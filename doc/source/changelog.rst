ChangeLog
^^^^^^^^^

0.4 series
==========
under development


0.3 series
==========

0.3.2 (2014-07-12)
------------------

* `#194 <https://bitbucket.org/hgvs/hgvs/issue/194/>`_: fix bug when reverse complementing nucleotides parsed from unicode

0.3.1 (2014-07-12)
------------------

* `#193 <https://bitbucket.org/hgvs/hgvs/issue/193/>`_: fix lookup table for NC_000014.8 (was .10)
* `#192 <https://bitbucket.org/hgvs/hgvs/issue/192/>`_: deprecated VariantMapper cache_transcripts param and replaced with always-on lru cache in uta data provider


0.3.0 (2014-06-19)
------------------

* `#103 <https://bitbucket.org/hgvs/hgvs/issue/103/>`_: significantly updated documentation
* `#162 <https://bitbucket.org/hgvs/hgvs/issue/162/>`_: provide simplified mapping interface, EasyVariantMapper
* `#171 <https://bitbucket.org/hgvs/hgvs/issue/171/>`_: integrate the data provider interface into hgvs, obsoleting bdi.  See hgvs.dataproviders.*
* `#177 <https://bitbucket.org/hgvs/hgvs/issue/177/>`_: rename mapping functions to x_to_y (dropping "hgvs" prefix)
* `#180 <https://bitbucket.org/hgvs/hgvs/issue/180/>`_: made set_uncertain an internal method (_set_uncertain)
* `#181 <https://bitbucket.org/hgvs/hgvs/issue/181/>`_: renamed hgvs.hgvsmapper.HGVSMapper to hgvs.variantmapper.VariantMapper
* `#184 <https://bitbucket.org/hgvs/hgvs/issue/184/>`_: rename HGVSPosition.seqref to ac
* `#185 <https://bitbucket.org/hgvs/hgvs/issue/185/>`_: enable validator to use HDPI to fetch sequence data; mfdb now required only for genomic sequences
* Makefile: print machine info during testing to calibrate/debug timing probs
* moved hgvs/data to hgvs/_data to emphasize it is internal and avoid tab completion on it
* remove unused args from VariantMapper.c_to_p()
* replace u1/uta1 references with hdp; update docs
* replaced bdi with hdp when referencing the data provider; tests pass
* setup.py: removed nose-timer (appeared to cause problems with pip install)
* standardize exception names with "HGVS" prefix
* updated examples/manuscript-example; other minor changes


0.2 series
==========

0.2.2 (2014-06-12)
------------------

* `#103 <https://bitbucket.org/hgvs/hgvs/issue/103/>`_: significantly updated documentation
* `#142 <https://bitbucket.org/hgvs/hgvs/issue/142/>`_: added BIC test cases
* `#167 <https://bitbucket.org/hgvs/hgvs/issue/167/>`_: disable the any_variant rule because it is confusing
* `#179 <https://bitbucket.org/hgvs/hgvs/issue/179/>`_: added quick and extra tags to tests; updated Makefile to support make test, test-quick, test-extra; removed test_hgvs_parser_real (but kept gcp version)
* added support for testing models ("models" attr and test-models)


0.2.1 (2014-06-11)
------------------

* `#157 <https://bitbucket.org/hgvs/hgvs/issue/157/>`_: don't reverse complement numeric "sequences" (as in del26)
* `#159 <https://bitbucket.org/hgvs/hgvs/issue/159/>`_: Update comment in tests/data/ADRA2B-dbSNP.tsv
* `#161 <https://bitbucket.org/hgvs/hgvs/issue/161/>`_: transform examples to sphinx doc (+upload)
* `#167 <https://bitbucket.org/hgvs/hgvs/issue/167/>`_: disable the any_variant rule because it is confusing
* `#175 <https://bitbucket.org/hgvs/hgvs/issue/175/>`_: added type to NADupN and Copy edit classes
* Added Important Notes section in README.rst
* Makefile: "test" target should depend on "setup" after all
* added example for stringification to README.rst
* added examples/Manuscript Example.ipynb
* added installation status (from hgvs-integration-test at travis-ci) and build status (from drone.io)
* hgvsmapper: use deepcopy when converting edits
* removed unused sphinx_pypi_upload.py
* updated examples to use uta1


0.2.0 (2014-03-09)
------------------

* updated README.rst example to use uta1; added .rst files to nosetest testing
* added ci-test-ve; switched to hgtools 5.0 use_vcs_version in setup.py
* take 1 on reconcililing test differences between internal jenkins and drone.io
* removed accidental tag (!); added sphinxcontrib-fulltoc to setup.py


0.1 series
==========

0.1.11 (2014-03-05)
-------------------

* removed accidental tag (!); added sphinxcontrib-fulltoc to setup.py
* updated package metadata; removed requirements.txt; tests pass


0.1.9 (2014-03-05)
------------------

* `#40 <https://bitbucket.org/hgvs/hgvs/issue/40/>`_: added additional tests
* `#114 <https://bitbucket.org/hgvs/hgvs/issue/114/>`_: add test that checks that all rules have been tested - and add tests for rules that were missed!
* `#135 <https://bitbucket.org/hgvs/hgvs/issue/135/>`_: add more tests; fixed and enabled tests previously commented out
* `#147 <https://bitbucket.org/hgvs/hgvs/issue/147/>`_: update tests to use updated sqlite test DB
* Added U14680.1 (BIC tx) to grammar test
* ExtrinsicValidator should not guess about bdi and mfdb sources; instead require caller to specify
* Fixed an un-handled case for parsing AA frameshifts - short form, e.g. "Ala97fs" (no alt AA).   Added tests.
* Makefile, setup,py, setup.cfg sync with sibling projects
* Merged hgvs_using_uta1 into default
* Merged in extrinsic_validation (pull request `#5 <https://bitbucket.org/hgvs/hgvs/issue/5/>`_)
* Remove redundant test
* added Validator class that wraps instrinsic and extrinsic validation
* added bdi accession testing
* added codeship status badge to README.rst, for testing
* added creating-a-variant example
* added sbin/get-dbsnp-tests-for-gene
* added tests from dbSNP for 6 new gene; fixed probs with uncertainty and Ter\d+ in existing tests
* bug fixes for uta1 integration; all tests pass except for sqlite db test
* checking cigar ref tgt orientation
* cigar intron count fix
* cut DNAH11 tests to representative set (apx 80% cut)
* finished integrating uta1 into hgvs and started updating tests
* fixed DNAH11-dbSNP tests
* fixed bug when falling off transcripts
* hgvsmapper is updated with uta1 requirements. testing modifications using hgvs-shell
* removed accession test from extrinsic validator (sequence lookup covers accession lookup)
* removed codeship badge
* renamed ~Validation to ~Validator to keep with class-as-actor naming scheme
* starting external validation with bdi
* testing
* trivial change to tickle codeship build
* updated edit type and tests to include identity for sub e.g., T>T
* updated external validation using bdi; added identity edit type for sub T>T; added HGVSValidationException class; added sample tests for mfdb
* updated package metadata; removed requirements.txt; tests pass
* upped bdi min version to >=0.1.0 (interface1)
* use pip installation status as build status since that's what users will experience
* working through updating TM and IM. HM g_to_c appears to work


0.1.8 (2014-01-22)
------------------

* updated README.rst example for bdi connect()


0.1.7 (2014-01-22)
------------------

* `#106 <https://bitbucket.org/hgvs/hgvs/issue/106/>`_, `#108 <https://bitbucket.org/hgvs/hgvs/issue/108/>`_: parse uncertain hgvsp/hgvsr; converter produces uncertain hgvsp.
* `#110 <https://bitbucket.org/hgvs/hgvs/issue/110/>`_, `#111 <https://bitbucket.org/hgvs/hgvs/issue/111/>`_: handle cases of entire gene deletion (p.0?) and stop codon in frame (p.?).   Updated tests.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_, `#89 <https://bitbucket.org/hgvs/hgvs/issue/89/>`_: can now parse Met1? and ext*N; removed extra fs parsing from delins.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: cleanup; AASub can go back to being a subclass of AARefAlt
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: def_p_pos needs to accept term13 as well as aa13 for ext; tests updated.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: fixed an ordering bug; added tests.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: fs/ext are now their own pro_edit types; they correspond to their own class objects.    5' extensions and 3' extensions can be parsed.   Tests updated.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: should be stringifying * as Ter; fixed code in 2 lines & tests in many.
* `#65 <https://bitbucket.org/hgvs/hgvs/issue/65/>`_: tighten ext rules; require a number for new start positions.
* `#90 <https://bitbucket.org/hgvs/hgvs/issue/90/>`_: added dup in hgvsmapper; allowed rev complement util to handle None (was triggering exceptions); added tests for dup.
* `#91 <https://bitbucket.org/hgvs/hgvs/issue/91/>`_: add extension support for parsing copyN and DupN
* `#91 <https://bitbucket.org/hgvs/hgvs/issue/91/>`_: make adding default totally extendable by allowing additional imports for the base grammar (default empty list)
* `#91 <https://bitbucket.org/hgvs/hgvs/issue/91/>`_: simplest implementation of parsing copyN, dupN - added directly to grammar (no extension)
* `#99 <https://bitbucket.org/hgvs/hgvs/issue/99/>`_: fix aa13t parsing
* `#99 <https://bitbucket.org/hgvs/hgvs/issue/99/>`_: fix aa13t parsing, take 2; tests pass (including G* test)
* `#99 <https://bitbucket.org/hgvs/hgvs/issue/99/>`_: re-enable tests related to this issue.
* Fixed a bug where del5insT was getting stringified as "5>T"
* added datum to range checking
* added datum to range checking
* added edit type as a property to the edit object; updated tests; added examples to hgvs-shell
* added edit type as a property to the edit object; updated tests; added examples to hgvs-shell
* close anonymous branch
* closed experimental dev branch
* closed hgvsvalidator feature branch on wrong default branch (grafted to default)
* doc updates and Makefile fix after fouled merge
* fixed minor doc typos
* hgvsc_to_hgvsp - ac defaults to None; seems better than forcing the user to pass 'None' as a param if they want the protein accession looked up.
* iv grammar branch
* make doc is broken & not used; removing it from make ci-test for now.
* merged in validator (pull request `#4 <https://bitbucket.org/hgvs/hgvs/issue/4/>`_)
* minor change to rebase
* removed links section from README
* renamed hgvsvalidator to validator and corresponding test; corrected start-end check added tests
* revised intrinsic validator and tests; deleted requests from setup.py
* updated README.rst example for bdi connect()
* updated docs to point back to pythonhosted
* updated installation.rst
* updated ipython notebook examples
* updated railroad building
* updated railroad in docs
* updated the fragile railroad building again


0.1.6 (2014-01-11)
------------------

* updated docs to point back to pythonhosted
* added setuptools to requirements.txt
* updated requirements.txt
* fixed bug in setup.py re: classifiers


0.1.5 (2014-01-11)
------------------

* fixed bug in setup.py re: classifiers


0.1.4 (2014-01-11)
------------------

* `#97 <https://bitbucket.org/hgvs/hgvs/issue/97/>`_: a bagillion doc updates; branch closed


0.1.3 (2014-01-11)
------------------

* `#60 <https://bitbucket.org/hgvs/hgvs/issue/60/>`_: 1st stab at grammar tests from the bottom-up (through locations/definite positions).   (See header in test_hgvs_grammar_full.py for details.)   Also added a few error checking tests.
* `#60 <https://bitbucket.org/hgvs/hgvs/issue/60/>`_: drop None from SequenceVariant (use case - only parsing an edit); grammar update for offset
* `#60 <https://bitbucket.org/hgvs/hgvs/issue/60/>`_: implement cleanup; distributed remaining items to separate issues.
* `#73 <https://bitbucket.org/hgvs/hgvs/issue/73/>`_: migrate hgvs to bdi-based protein accession lookup
* `#90 <https://bitbucket.org/hgvs/hgvs/issue/90/>`_: fixed typo for delins and ins for parsing hgvsp
* `#92 <https://bitbucket.org/hgvs/hgvs/issue/92/>`_: add a subclass of AARefAlt (AASub) which overrides __str__ to get the representation right; grammar update
* `#92 <https://bitbucket.org/hgvs/hgvs/issue/92/>`_: fix error in NARefAlt
* `#93 <https://bitbucket.org/hgvs/hgvs/issue/93/>`_: added *variant* liftover for HGVS projector, with tests
* `#93 <https://bitbucket.org/hgvs/hgvs/issue/93/>`_: implemented HGVS projector for interval liftover
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: cleanup and test update
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: deleting tests/data
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: fix file
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: name cleanup
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: removed nightly test target
* `#96 <https://bitbucket.org/hgvs/hgvs/issue/96/>`_: short set of real data for gcp parsing
* `#97 <https://bitbucket.org/hgvs/hgvs/issue/97/>`_: a bagillion doc updates; branch closed
* `#97 <https://bitbucket.org/hgvs/hgvs/issue/97/>`_: major doc restructuring, cleanup, additions
* A few more basic tests
* Add parser test which just tries to parse all the cvids (g, c and p) - currently skips unsupported forms.   Also tweaked the r variants in the all cvid file (T should be U).
* Add some basic intervalmapper tests based on the coverage results
* Fill in more protein edit tests
* Fixed a bug breaking n_edit and m_edit; updated tests.
* Make documentation more Sphinx-friendly
* More grammar tests; simplified dup check for hgvsc to p conversion
* Tweak HGVSp expected so an edit creating a stop codon is represented by Ter instead of * (to match hgvs string code)
* add alternative UTA_DB_URL options to Makefile; cleanup eggs in cleanest (not cleaner) and bdist et al. in cleaner (not cleanest)
* added .travis.yml
* added a projector example
* added classifiers and keywords to setup.py
* added license to docs
* added railroad diagram to docs
* additional grammar tests - HGVS edits are failing commented out for now
* bug fix: make test was running nightly tests
* build reST doc for railroad grammar
* code cleanup
* commenting out test until I am in a place where I can run it
* doc updates
* eliminated most sphinx warnings
* lots of doc restructuring and consolidation
* minor cleanup
* more grammar tests
* removed reST examples
* sync default into branch
* sync default into dev
* updated README with pypi info
* updated installation
* updated misc/hgvs-shell for new bdi.uta0.connect()
* updated railroad diagram to include version number
* updated sphinx doc/source/conf.py
* yet more doc changes


0.1.2 (2014-01-05)
------------------

* `#85 <https://bitbucket.org/hgvs/hgvs/issue/85/>`_: adapted hgvs to bdi with runtime-selectable UTA connections
* updated README with pypi info
* doc updates
* now depend on uta and bdi from PyPI (not dependency_links); sync'd Makefile and setup.py with uta; updated test and docs targets


0.1.1 (2014-01-03)
------------------

* `#64 <https://bitbucket.org/hgvs/hgvs/issue/64/>`_: handle the following: (1) indel crosses stop codon; (2) indel crosses start codon; need to retest on full suite
* `#64 <https://bitbucket.org/hgvs/hgvs/issue/64/>`_: update 4 tests to reflect p.Met1? behavior for deletions crossing from 5'utr to cds:
* `#83 <https://bitbucket.org/hgvs/hgvs/issue/83/>`_: cleanup fs* cases where mutalyzer assigns fs*N where N = end of transcript instead of an actual stop codon (expected result is now fs*?)
* `#83 <https://bitbucket.org/hgvs/hgvs/issue/83/>`_: comment out tests that need review/cleanup (and added comment); fixed tests where expected result was incorrect (still need to check tests w/ no expected result)
* `#83 <https://bitbucket.org/hgvs/hgvs/issue/83/>`_: fill in intronic variants with expected hgvsp results (p.?) per curators
* `#84 <https://bitbucket.org/hgvs/hgvs/issue/84/>`_: ext with no stop codons are represented as ext*? - updated tests accordingly
* `#84 <https://bitbucket.org/hgvs/hgvs/issue/84/>`_: fix expected result
* Turn off dbg
* Turn off more dbg
* added *lots* of documentation
* added Apache license and code boilerplate to all source files and scripts
* doc updates
* fix coverage by calling tests via python setup.py nosetest; fix  test name
* logo: rotated, moved to subdir, created favicon
* made png and ico logos transparent
* moved sphinx sources to doc/source and updated configs
* now depend on uta and bdi from PyPI (not dependency_links); sync'd Makefile and setup.py with uta; updated test and docs targets
* removed test-setup-coverage from Makefile dependencies (put in setup.py instead)
* s/locusdevelopment/invitae/
* updated doc static images
* updated hgvs-logo.png per Makefile
* updated setup.py "license" attribute
* vastly improved sphinx documentation. More to do


0.1.0 (2013-12-30)
------------------

* `#52 <https://bitbucket.org/hgvs/hgvs/issue/52/>`_: generate syntax/railroad diagrams (in misc/railroad/)
* `#56 <https://bitbucket.org/hgvs/hgvs/issue/56/>`_: updated tests; fixed fs*N (only one still broken)
* `#62 <https://bitbucket.org/hgvs/hgvs/issue/62/>`_: synchronized setup files among UTA program components
* `#66 <https://bitbucket.org/hgvs/hgvs/issue/66/>`_: added support for p.0, p.=, p.?, p.(=), p.(?), with tests
* `#66 <https://bitbucket.org/hgvs/hgvs/issue/66/>`_: updated grammar for p.0, p.=, p.?, p.(=), p.(?) to reject invalid p.(0), etc.
* `#72 <https://bitbucket.org/hgvs/hgvs/issue/72/>`_: update hgvs to use bdi (no direct connections to uta anymore)
* Close branch jenkins.
* Convert test input and consumer to use 4-column format
* Fix extension for frameshift case; update test to get around dupN (trim the N)
* Fix tag
* Last cleanup before merge
* README.rst: fixed preformatted text (that wasn't)
* Refactored cp tests to work from a common base which more closely resembles the gcp test.    All-CVID test input file is in 4-column format (lots of missing data, though)
* Revamp of c to p based on tests results; checkpoint.   Sanity & EH tests all run.
* Update makefile to include a mechanism for generating code coverage during tests
* Updated Makefile test task to skip tests prefixed with test_nightly; added task to run all;  enabled all cvid test to check this
* add missing files to package_data
* added Apache license and code boilerplate to all source files and scripts
* added architecture & dependency info to README.rst
* added comments to failed and broken tests
* added examples directory
* added sbin/test-runner (see script header for example)
* added setuptools>2.0 to setup.py (testing); updated README.rst
* close branch
* corrected minor README typo
* fix test
* fixed bug in reported AA edit for extensions
* fixed bug introduced in 63e0baf7c986; removed unnecessary and obsolete edti.interface import in tests/framework/mock_input_source.py
* fixed bug that caused protein accession to be not looked up when not specified
* fixed bug with unqualified class names in hgvs.pymeta
* hgvsc to hgvsp bug fixes/updates: changed del/dups to represent the c-terminal end; variants in utr, intron & 1st AA are treated as p.? (subject to review).  Cleaned up test data.   Tweaked seguid data so the tests pick up the correct NP in a case where there's more than one match - mainly just to get the tests to pass.
* hgvsc to p takes an accession
* make the nightly start from make cleanest (tougher)
* merge into default
* more README and setup.py updates
* move edti bits to bdi
* moved misc/hgvs-shell to sbin
* setup.py: testing yet another dependency_links format
* updated README.rst
* updated bdi and tests to use external UTA instance
* updated examples dir
* updated logo and README


0.0 series
==========

0.0.9 (2013-12-16)
------------------

* added comments to failed and broken tests
* renamed grammars to .pymeta
* consolidated g-c-p testing into a single test file; commented out putatively broken tests; DNAH11 works!
* add forgotten sbin/fasta-seguid for commit -2 (0d29d0ea2d42)
* fixed minor grammar bugs re: AA term and frameshift
* added accession lookup for all of RefSeq protein
* got 'make jenkins' target working
* harmonized with UTA Makefile and setup.py to try to get tests working
* added biopython to setup.py
* fixed pro_eq grammar bug mentioned in `#42 <https://bitbucket.org/hgvs/hgvs/issue/42/>`_
* Updated DNAH11 and NEFL tests.  They run, so I'll mark as complete, but there are errors associated with the proteins
* hgvsc_to_hgvsp: Fixed a delins bug
* hgvsc_to_hgvsp: Fixed bug in insertion indexing; improved exception handing
* added misc/hgvs-shell to simplify manual testing
* hgvs tests for DNAH11 and NEFL -> note protein not currently working just change if statement
* initial checkin for jenkins branch; want to test this in the build context
* Close branch c_to_p
* Merged in c_to_p (pull request `#3 <https://bitbucket.org/hgvs/hgvs/issue/3/>`_)
* Incorporate AASpecial; tests pass.
* merge from default
* merged default into c_to_p
* added AASpecial to handle p.=, p.?, p.0 (and parenthesized versions)
* fixed setup.py issue that caused omission of hgvs.utils on install
* Forgot to add a test file to mercurial
* Merged from default; fixed a test.
* Make test file name more consistent
* SImplified comparison in the event of a simple substitution; updated tests so the failed tests are commented out.
* Reformatted Emily's test data to make it more consumer-friendly; continuous test tweaking - latest checkpoint.
* Another couple of fixes based on EH tests; checking in working version of the tests.
* updated hgvsmapper with all g<->r<->c transformations
* remove explicit class references from makeGrammar invocation, require fully-qualified class name in hgvs.ometa
* close uncertainty branch
* added chr_to_NC in utils, added c_to_g in hgvsmapper
* Name cleanup for tests
* Tests now play nicely with both real data and the mock data.
* Add call to get_tx_seq()
* Missed a rename in the tests.
* Rename test classes to be a bit more consistent with their use.
* Inserted hgvsc_to_hgvsp into hgvsmapper.
* merge from default
* align with developer.rst conventions on naming hgvs variants vs. strings
* Fix tests to run in makefile context; some more documentation
* revamped hgvs_c_to_p so its interface matches hgvsmapper; should make incorporation a simple matter of copying the hgvsc_to_hgvsp method in.    Updated tests accordingly.    Moved tests to top-level.
* Merge from default
* Re-arranging code for utils/staging for hgvs mapper.
* Purged debug code
* Ack - last checkin broke the tests; fixed accession setup
* format cleanup
* Incorporate stopgap for protein accession; refactor so interface consumes data in the current UTA format; refactor tests to mimic UTA input; getting actual seq is still a placeholder.
* merging default into c_to_p
* added location uncertainty (parsing, representation, formatting, testing)
* added multifastadb code and tests
* [mq]: hgvsmapper-work
* imported patch hgvs-utils-dir
* added multifastadb tool and tests
* added Rudy's AA p.= rule
* [mq]: grammar-relo
* added hgvs.stopgap
* Close branch transcriptmapper
* Merged in transcriptmapper (pull request `#2 <https://bitbucket.org/hgvs/hgvs/issue/2/>`_)
* added TODO for tracking, prior to merging pull request
* Basic handling of variants in non-coding regions; will return p.= in all cases; this does not handle the case where a 5'utr variant results in the creation of an upstream Met.
* merged with default, TM bug fixes and more tests
* cleanup names (or at least make them a little more descriptive)
* added tm.cds_start_i in place of hard coding cds
* refactoring
* Roll back exon-specific changes and assume input is entire transcript concatenated together; retain the transcript data as recordtype
* fix test for AA in 2nd exon
* Convert transcript data object to recordtype; add tests for multi-exon (in progress)
* more tests
* additional TM fixes and more tests with multiple exons and strands
* Account for transcripts w/ more than 1 exon (test input assumed one)
* added some 1-exon tests
* Incorporate aa util and extend interval class (for test data); convert code to produce SequenceVariant objects for hgvs c to p.   Also hacked in a way to handle p.= into the grammar (should be reviewed before merge).
* bug fixes
* Merged default into c_to_p
* added enum to transcriptmapper tests
* Last cleanup before merging default into here
* all input/output is hgvs-based. updated tests accordingly
* Close branch protein-variants
* Merged in protein-variants (pull request `#1 <https://bitbucket.org/hgvs/hgvs/issue/1/>`_)
* hgvs.edit: fixed and improved fs handling, and added mediocre tests
* hgvs.utils: added Xaa=X, Ter=*, Sec=U for aa1-to-aa3 & aa3-to-aa1 translation
* code cleaning
* finished tests for transcriptmapper
* finished all the g,r,c conversions adding more tests
* More cleanup; simplify variant inserter code
* updated transcriptmapper to support g->r, r->g, r->c and appropriate tests
* minor cleanup
* variant insert tests
* merged edti-uta0 branch
* closing branch prior to merge
* edti: added __metaclass__ to edti.interface; added fetch_gene_info to uta0
* hgvs.edti: EDTI base interface and UTA0 implementation milestone
* hgvs.parser: add function attributes for every rule to enable, e.g., Parser.parse_c_interval(...)
* implemented p. parsing and formatting, with tests
* hgvs.utils: handle case when aa string is None
* hgvs.utils: added aa_to_aa{1,3} functions to coerce to 1- or 3-letter amino acids
* hgvs.utils: added protein 1-letter and 3-letter conversion
* Checkpoint for new branch (hgvs c to p)
* branched transcriptmapper
* improved parsing of hgvs_position rules (i.e., without edits) to handle g,m,n,r,c,p types distinctly
* added {gmn,c,r,p}_edit rule to parse variants without accesssions (e.g., c.76A>T)
* renamed DelIns class to RefAlt
* renamed Variant to SequenceVariant, and instance variant seqref to ac
* closed abandoned protein-support branch
* updated parser tests to include aspirational and "reject" tests
* [mq]: import-location-changes
* [mq]: import
* hgvs.location: renamed location classes; added BaseOffset position for r. and c.; removed predicate methods (is_exonic, etc);
* incomplete, buggy milestone
* setup.py: use full path for doc/description.rst
* updated CDSPosition to include datum and added tests
* use get_distribution() rather than require() to fetch version
* Fix for pathing to grammar.txt from within hgvs.parser.Parser
* modified setup.py to zipsafe false
* TODO edited online with Bitbucket
* Making setup.py file pathing absolute
* Fix for setup.py
* updated Makefile and setup.py
* revert directory to current after upload
* fixed bug in HGVSPosition.__str__ and added HGVSPosition test


0.0.7 (2013-10-11)
------------------

* fixed bug in HGVSPosition.__str__ and added HGVSPosition test
* collapsed grammar cases for c_pos; fixed variant test case typo


0.0.6 (2013-10-11)
------------------

* collapsed grammar cases for c_pos; fixed variant test case typo
* updated docs; fixed typo in variant


0.0.5 (2013-10-11)
------------------

* updated docs; fixed typo in variant
* added HGVSPosition (aka HGVS Lite)


0.0.4 (2013-10-11)
------------------

* added HGVSPosition (aka HGVS Lite)
* "simple" (single site) variants now pass tests
* update hgvs.__init__ and sphinx to use version from hgtools


0.0.3 (2013-10-10)
------------------

* update hgvs.__init__ and sphinx to use version from hgtools
* removed home-grown hg versioning in favor of hgtools
* removed virtualenv support and cleaned up Makefile
* milestone sync; c, gmn, and r types mostly work; some tests broken
* updated variant and added test
* updated grammar (more to do) and tests
* added hgvs.posedit and tests
* updated hgvs.edit
* removed CDSInterval (will use Interval for all intervals)
* fixed typo
* update hgvs.location and tests
* minor setup.py changes


0.0.2 (2013-09-20)
------------------

* minor setup.py changes
* grammar simplification; added Laros grammar, examples, comments
* Reverted Lawrence's changes to edit.py (after discussing with him).
* Adding some convenience properties to be used in Geneticus.
* updated grammar; added README.rst
* added missing deps to setup.py; switched to plain ole distutils
* added developer notes, logo, sphinx config


0.0.1 (2014-08-01)
------------------

* initial commit
