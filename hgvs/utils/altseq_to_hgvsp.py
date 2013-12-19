#
# Utility class for creating an hgvsp SequenceVariant object,
# given a transcript with variants applied.
# Used in hgvsc to hgvsp conversion.
#
import collections
import difflib

import hgvs.edit
import hgvs.exceptions
import hgvs.location
import hgvs.posedit
import hgvs.utils
import hgvs.variant

DBG = False

class AltSeqToHgvsp(object):

    def __init__(self, ref_data, alt_data):
        """Constructor

        :param ref_data: reference transcript record
        :type recordtype
        :param alt_data: alt transcript record
        :type recordtype
        """
        self._ref_data = ref_data
        self._alt_data = alt_data
        self._protein_accession = self._ref_data.protein_accession
        self._ref_seq = self._ref_data.aa_sequence
        self._alt_seq = self._alt_data.aa_sequence
        self._frameshift_start = self._alt_data.frameshift_start
        self._is_substitution = self._alt_data.is_substitution
        self._is_ambiguous = self._alt_data.is_ambiguous

        if DBG:
            print len(self._ref_seq), len(self._alt_seq), self._frameshift_start, self._protein_accession
            print self._ref_seq
            print self._alt_seq
            print "aa variant start: {}".format(self._alt_data.variant_start_aa)
            print self._ref_data.transcript_sequence
            print self._alt_data.transcript_sequence

    def build_hgvsp(self):
        """Compare two amino acid sequences; generate an hgvs tag from the output

        :return list of variants in sequence order
        :type list of dict
        """

        variants = []

        if not self._is_ambiguous:

            do_delins = True
            if self._ref_seq == self._alt_seq:
                do_delins = False
            elif self._is_substitution:
                if len(self._ref_seq) == len(self._alt_seq):
                    diff_pos = [(i, self._ref_seq[i], self._alt_seq[i]) for i in xrange(len(self._ref_seq))
                                if  self._ref_seq[i] != self._alt_seq[i]]
                    if len(diff_pos) == 1:
                        (start, deletion, insertion) = diff_pos[0]
                        variants.append({"start": start + 1, "ins": insertion, "del": deletion})
                        do_delins = False

                elif self._alt_seq[self._alt_data.variant_start_aa - 1] == "*" and \
                                self._ref_seq[self._alt_data.variant_start_aa - 1] != "*": # introduced stop codon
                    deletion = self._ref_seq[self._alt_data.variant_start_aa - 1:]
                    variants.append({"start": self._alt_data.variant_start_aa, "ins": "*", "del": deletion})
                    do_delins = False

            if do_delins:
                if self._alt_data.is_frameshift:
                    start = self._alt_data.variant_start_aa - 1
                    aa_start = self._alt_data.variant_start_aa
                    while self._ref_seq[start] == self._alt_seq[start]:
                        start += 1
                        aa_start += 1
                    insertion = list(self._alt_seq[start:])
                    deletion = list(self._ref_seq[start:])
                    variants.append({"start": aa_start, "ins": insertion, "del": deletion})

                else: # non-frameshifting delins or dup
                    # get size diff from diff in ref/alt lengths
                    start = self._alt_data.variant_start_aa - 1
                    aa_start = self._alt_data.variant_start_aa
                    delta = len(self._alt_seq) - len(self._ref_seq)
                    while self._ref_seq[start] == self._alt_seq[start]:
                        start += 1
                        aa_start += 1
                    offset = start + abs(delta)

                    if delta > 0:   # net insertion
                        insertion = list(self._alt_seq[start:offset])
                        deletion = []
                        ref_sub = self._ref_seq[start:]
                        alt_sub = self._alt_seq[offset:]
                    elif delta < 0: # net deletion
                        insertion = []
                        deletion = list(self._ref_seq[start:offset])
                        ref_sub = self._ref_seq[offset:]
                        alt_sub = self._alt_seq[start:]
                    else:
                        insertion = []
                        deletion = []
                        ref_sub = self._ref_seq[start:]
                        alt_sub = self._alt_seq[start:]

                    # from start, get del/ins out to last difference
                    diff_indices = [i for i in xrange(len(ref_sub)) if ref_sub[i] != alt_sub[i]]
                    if diff_indices:
                        max_diff = diff_indices[-1] + 1
                        insertion.extend(list(alt_sub[:max_diff]))
                        deletion.extend(list(ref_sub[:max_diff]))

                    variants.append({"start": aa_start, "ins": insertion, "del": deletion})

            if DBG:
                print variants

        if self._is_ambiguous:
            var_ps = [self._create_variant('', '', '', '', acc=self._protein_accession,
                                           is_ambiguous=self._is_ambiguous)]
        elif variants:
            var_ps = [self._convert_to_sequence_variants(x, self._protein_accession) for x in variants]
        else:    # ref = alt - "silent" hgvs change
            var_ps = [self._create_variant('', '', '', '', acc=self._protein_accession)]

        # TODO - handle multiple variants

        if len(var_ps) > 1:
            raise hgvs.exceptions.HGVSError("Got multiple AA variants - not supported")
        return var_ps[0]

    #
    # internal methods
    #

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
            aa_start = aa_end = hgvs.location.AAPosition(base=start, aa=deletion[0])
            ref = ''

            if start == 1:
                ref = ''
                alt = ''
                self._is_ambiguous = True   # side-effect
            elif start == len(self._ref_seq):                           # extension at stop codon
                len_ext = len(insertion) - len(deletion) # don't include the former stop codon
                subst_at_stop_codon = insertion[0]

                aa_start = aa_end = hgvs.location.AAPosition(base=start, aa='*')
                ref = ''
                alt = subst_at_stop_codon
                fs = 'ext*{}'.format(len_ext)
            else:
                try:
                    new_stop = str(insertion.index("*") + 1)    # start w/ 1st change; ends w/ * (inclusive)
                except ValueError:
                    new_stop = "?"

                if new_stop != "1":
                    alt = insertion[0]
                    fs = 'fs*{}'.format(new_stop)

                else:   # frameshift introduced stop codon at variant position
                    alt = '*'

        elif start == 1:                                          # initial methionine is modified
                aa_start = aa_end = hgvs.location.AAPosition(base=start, aa=deletion)
                ref = ''
                alt = ''
                self._is_ambiguous = True   # side-effect
        else:                                                           # no frameshift
            if len(insertion) == len(deletion) == 1:                    # substitution
                aa_start = aa_end = hgvs.location.AAPosition(base=start, aa=deletion)
                ref = ''
                alt = insertion

            elif len(deletion) > 0:                                     # delins OR deletion OR stop codon at variant position
                ref = deletion
                end = start + len(deletion) - 1
                if len(insertion) > 0:                                  # delins
                    aa_start = hgvs.location.AAPosition(base=start, aa=deletion[0])
                    if end > start:
                        aa_end =  hgvs.location.AAPosition(base=end, aa=deletion[-1])
                    else:
                        aa_end = aa_start
                    alt = insertion

                else:                                                   # deletion OR stop codon at variant position
                    if len(deletion) + start == len(self._ref_seq):     # stop codon at variant position
                        aa_start = hgvs.location.AAPosition(base=start, aa=deletion[0])
                        aa_end = hgvs.location.AAPosition(base=start, aa=deletion[0])
                        ref = ''
                        alt = '*'
                    else:                                               # deletion
                        aa_start = hgvs.location.AAPosition(base=start, aa=deletion[0])
                        if end > start:
                            aa_end =  hgvs.location.AAPosition(base=end, aa=deletion[-1])
                        else:
                            aa_end = aa_start
                        alt = None

            elif len(deletion) == 0:                                    # insertion OR duplication OR extension

                is_dup, dup_start = self._check_if_ins_is_dup(start, insertion)

                if is_dup:                                              # duplication
                    dup_end = dup_start + len(insertion) - 1
                    aa_start = hgvs.location.AAPosition(base=dup_start, aa=insertion[0])
                    aa_end =  hgvs.location.AAPosition(base=dup_end, aa=insertion[-1])
                    ref = alt = None

                else:                                                   # insertion OR extension
                    if start == len(self._ref_seq):                     # extension
                        len_ext = len(insertion) # don't include the former stop codon
                        subst_at_stop_codon = insertion[0]

                        aa_start = aa_end = hgvs.location.AAPosition(base=start, aa='*')
                        ref = ''
                        alt = subst_at_stop_codon
                        fs = 'ext*{}'.format(len_ext)

                    else:                                               # insertion
                        start = start - 1
                        end = start + 1

                        aa_start = hgvs.location.AAPosition(base=start, aa=self._ref_seq[start - 1])
                        aa_end =  hgvs.location.AAPosition(base=end, aa=self._ref_seq[end - 1])
                        ref = None
                        alt = insertion

            else: # should never get here
                raise ValueError("unexpected variant: {}".format(variant))

        var_p = self._create_variant(aa_start, aa_end, ref, alt, fs, is_dup, acc, is_ambiguous=self._is_ambiguous)

        return var_p

    def _check_if_ins_is_dup(self, start, insertion):
        """Helper to identify an insertion as a duplicate

        :param start 1-based insertion start
        :type int
        :param insertion sequence
        :type str
        :return (is duplicate, variant start)
        :type (bool, int)
        """
        is_dup = False  # assume no
        variant_start = None

        # dup before?
        dup_candidate_start = start - len(insertion) - 1
        dup_candidate = self._ref_seq[dup_candidate_start: dup_candidate_start + len(insertion)]
        if insertion == dup_candidate:
            is_dup = True
            variant_start = dup_candidate_start + 1

        # dup after?
        dup_candidate_start = start - 1
        dup_candidate = self._ref_seq[dup_candidate_start: dup_candidate_start + len(insertion)]
        if insertion == dup_candidate:
            is_dup = True
            variant_start = dup_candidate_start + 1

        return is_dup, variant_start

    def _create_variant(self, start, end, ref, alt, fs=None, is_dup=False, acc=None, is_ambiguous=False):
        """Creates a SequenceVariant object"""
        interval = hgvs.location.Interval(start=start, end=end)
        if is_ambiguous:
            edit = hgvs.edit.AASpecial(status='?')
        elif is_dup:
            edit = hgvs.edit.Dup()
        elif ref == alt == '':
            edit = hgvs.edit.AASpecial(status='=')
        else:
            edit = hgvs.edit.AARefAlt(ref=ref, alt=alt, fs=fs)
        posedit = hgvs.posedit.PosEdit(interval, edit)
        var_p = hgvs.variant.SequenceVariant(acc, 'p', posedit)

        return var_p

