#
# builds an hgvsp SequenceVariant object for a modified transcript sequence based on incorporated variants
#
import collections
import difflib

import hgvs.edit
import hgvs.location
import hgvs.posedit
import hgvs.utils
import hgvs.variant

class AltSeqToHgvsp(object):

    def __init__(self, ref_seq, alt_seq, protein_accession, frameshift_start = None):
        """Constructor

        The normal difflib comparison may identify islands of matches in a frameshift
        which will end up being reported as multiple variants.

        :param ref_seq: protein reference sequence
        :type str
        :param alt_seq: protein alternate sequence
        :type str
        :param frameshift_start: index n protein (1-based) where a frameshift should affect all downstream bases
        :type int
        """
        self._ref_seq = ref_seq
        self._alt_seq = alt_seq
        self._frameshift_start = frameshift_start
        self._protein_accession = protein_accession

    def build_hgvsp(self):
        """Compare two amino acid sequences; generate an hgvs tag from the output

        :return list of variants in sequence order
        :type list of dict
        """

        indel_map = {'+':'ins', '-':'del'}

        diff_list = difflib.Differ().compare(self._ref_seq, self._alt_seq)

        # walk through the difflib string list and summarize variants as they are encountered
        ref_index = 1
        alt_index = 1
        in_variant = False
        variants = []
        for item in diff_list:
            change = item[0]
            if change == ' ':       # a match
                if in_variant:      # process the variant just exited
                    in_variant = False
                    variants.append(current_var)
                ref_index += 1
                alt_index += 1
            else:                   # a mismatch
                base = item[-1]
                if not in_variant:  # start a new variant
                    in_variant = True
                    current_var = collections.defaultdict(list)
                    current_var['start'] = ref_index

                    if self._frameshift_start and current_var['start'] >= self._frameshift_start:
                        current_var = self._force_variant_to_frameshift(current_var, ref_index, alt_index)
                        variants.append(current_var)
                        in_variant = False
                        break

                current_var[indel_map[change]].append(base)
                if change == '-':
                    ref_index += 1
                elif change == '+':
                    alt_index += 1


        if in_variant:  # implies end of a frameshift; need to add this last variant to the list
            variants.append(current_var)

        if variants:
            sequence_variants = [self._convert_to_sequence_variants(x, self._protein_accession) for x in variants]
        else:    # create a "silent" variant
            sequence_variants = [self._create_variant('', '', '', '', acc=self._protein_accession)]

        # TODO - handle multiple variants
        return sequence_variants[0]

    #
    # internal methods
    #

    def _force_variant_to_frameshift(self, current_variant, ref_index, alt_index):
        """Make this variant a terminal frameshift

        :param current_variant: representation of variant to describe as a frameshift
        :type dict
        :param ref_index: reference sequence index (1-based) where frameshift starts
        :type int
        :param alt_index:  alt sequence index (1-based) where frameshift starts
        :type int
        :return updated current_variant
        :type dict
        """
        current_variant['del'] = list(self._ref_seq[ref_index - 1:])
        current_variant['ins'] = list(self._alt_seq[alt_index - 1:])
        return current_variant

    def _convert_to_sequence_variants(self, variant, acc):
        """Convert AA variant to an hgvs representation

        :param variant: contains start, del, and ins
        :type dict
        :param acc: protein accession
        :type str
        :return hgvs string
        """
        start = variant['start']
        insertion = ''.join(variant['ins'])
        deletion = ''.join(variant['del'])

        is_frameshift = insertion and deletion and deletion[-1] == '*'

        # defaults
        is_dup = False  # assume not dup
        fs = None

        if is_frameshift:                                               # frameshift
            aa_start = aa_end = hgvs.location.AAPosition(pos=start, aa=deletion[0])
            ref = ''

            try:
                new_stop = str(insertion.index("*") + 1)    # start w/ 1st change; ends w/ * (inclusive)
            except ValueError:
                new_stop = "?"

            if new_stop != "1":
                alt = insertion[0]
                fs = 'fs*{}'.format(new_stop)

            else:   # frameshift introduced stop codon at variant position
                alt = '*'

        else:                                                           # no frameshift
            if len(insertion) == len(deletion) == 1:                    # substitution
                aa_start = aa_end = hgvs.location.AAPosition(pos=start, aa=deletion)
                ref = ''
                alt = insertion

            elif len(deletion) > 0:                                     # delins OR deletion
                ref = ''
                aa_start = hgvs.location.AAPosition(pos=start, aa=deletion[0])

                end = start + len(deletion) - 1
                if len(insertion) > 0:                                  # delins
                    if end > start:
                        aa_end =  hgvs.location.AAPosition(pos=end, aa=deletion[-1])
                    else:
                        aa_end = aa_start
                    alt = insertion

                else:                                                   # deletion OR stop codon at variant position
                    if len(deletion) + start == len(self._ref_seq):     # stop codon at variant position
                        aa_end = hgvs.location.AAPosition(pos=start, aa=deletion[0])
                        alt = '*'
                    else:                                               # deletion
                        if end > start:
                            aa_end =  hgvs.location.AAPosition(pos=end, aa=deletion[-1])
                        else:
                            aa_end = aa_start
                        alt = None

            elif len(deletion) == 0:                                    # insertion OR duplication OR extension

                is_dup, dup_start = self._check_if_ins_is_dup(start, insertion, self._ref_seq)

                if is_dup:                                              # duplication
                    dup_end = dup_start + len(insertion) - 1
                    aa_start = hgvs.location.AAPosition(pos=dup_start, aa=insertion[0])
                    aa_end =  hgvs.location.AAPosition(pos=dup_end, aa=insertion[-1])
                    ref = alt = None

                else:                                                   # insertion OR extension
                    if start == len(self._ref_seq):                     # extension
                        len_ext = len(insertion) # don't include the former stop codon
                        subst_at_stop_codon = insertion[-1]

                        aa_start = aa_end = hgvs.location.AAPosition(pos=start, aa='*')
                        ref = ''
                        alt = subst_at_stop_codon
                        fs ='ext*{}'.format(len_ext)

                    else:                                               # insertion
                        end = start + 1

                        aa_start = hgvs.location.AAPosition(pos=start, aa=self._ref_seq[start - 1])
                        aa_end =  hgvs.location.AAPosition(pos=end, aa=self._ref_seq[end - 1])
                        ref = None
                        alt = insertion

            else: # should never get here
                raise ValueError("unexpected variant: {}".format(variant))

        var_seq = self._create_variant(aa_start, aa_end, ref, alt, fs, is_dup, acc)

        return var_seq


    def _check_if_ins_is_dup(self, start, insertion, ref_seq):
        """Helper to identify an insertion as a duplicate"""
        is_dup = False  # assume no
        variant_start = None

        if len(insertion) == 1:  # since difflib may match 1-AA dups before or after, need to check both
            ref_prev = ref_seq[start - 2]
            ref_next = ref_seq[start - 1]
            if insertion == ref_prev or insertion == ref_next:
                is_dup = True
                variant_start = start - 1 if insertion == ref_prev else start

        else:
            # figure out the candidate ref positions that should match if the insertion is a dup
            dup_candidate_start = start - len(insertion) - 1
            dup_candidate_end = dup_candidate_start + len(insertion)
            dup_candidate = ref_seq[dup_candidate_start: dup_candidate_end]

            if insertion == dup_candidate:
                is_dup = True
                variant_start = dup_candidate_start + 1

        return is_dup, variant_start

    def _create_variant(self, start, end, ref, alt, fs=None, is_dup=False, acc=None):
        """Creates a SequenceVariant object"""
        interval = hgvs.location.Interval(start=start, end=end)
        if is_dup:
            edit = hgvs.edit.Dup()
        else:
            edit = hgvs.edit.AARefAlt(ref=ref, alt=alt, fs=fs)
        posedit = hgvs.posedit.PosEdit(interval, edit)
        var = hgvs.variant.SequenceVariant(acc, 'p', posedit)

        return var


def main():
    pass


if __name__ == "__main__":
    main()
