# Milestone 2 — Consolidated Contract Test Results

Prepared 15 October 2026. **63 unique contracts: 43 previously tested and 20 newly tested.** This report selects one latest available saved result per contract, not every historical rerun. No previously tested contract was sent to Gemini for this reporting task. Historical JSON reports and findings were preserved; no old results were re-extracted or re-scored for this report.

## Closure decision

**Milestone 2 is complete for the agreed batch-processing and evaluation scope.** The runner processes folders, isolates individual failures, saves per-contract reports and batch summaries, tracks time/tokens, and exposes review reasons. Automated verification: 33 tests and lint checks pass. This is a learning-project milestone closure, not a claim of perfect extraction accuracy or complete agreement with CUAD.

Known limitations remain documented below: agreement-date conventions differ from signature-date labels in some CUAD answers; party-list and multi-jurisdiction representations are not fully normalized; collective-party cleanup can mishandle combined name/description entries; quote presence does not prove semantic support. These should remain regression/review cases during subsequent milestones.

## How to read this report

- **Extracted** is the value saved from Gemini. **Reference** is the reference representation used by that saved evaluator. The original parties answer is also shown where it was retained in that report.
- **Mismatch** does not establish model error. Review findings distinguish source-supported values, annotation differences, date-policy disagreement, and evaluator limitations.
- **Unscored** means the saved evaluator could not reliably compare a reference (for example, an incomplete date). Missing in both extraction and reference is counted separately from populated-field matches.
- Results are separated by extraction cohort. Historical prompt results were not rerun with the revised prompt. There is no pooled accuracy percentage across these versions. Cohort counts are deduplicated latest-record subsets, not original complete batch counts.
- One company can have multiple different contracts in different cohorts. The samples were development selections, not independent representative benchmark samples.

## Cohort statistics

Populated, scorable reference fields only:

| Saved-result cohort | Contracts | Parties | Agreement date | Governing law | Unscored fields |
| --- | ---: | --- | --- | --- | ---: |
| Initial MVP | 1 | 0/1 (0.0%) | 1/1 (100.0%) | 1/1 (100.0%) | 0 |
| Earlier prompt | 23 | 13/23 (56.5%) | 17/17 (100.0%) | 12/19 (63.2%) | 4 |
| Revised prompt — regression | 9 | 5/8 (62.5%) | 8/8 (100.0%) | 6/6 (100.0%) | 0 |
| Revised prompt — first unseen set | 10 | 6/10 (60.0%) | 9/9 (100.0%) | 5/9 (55.6%) | 0 |
| Revised prompt — final unseen set | 20 | 15/20 (75.0%) | 14/16 (87.5%) | 8/12 (66.7%) | 4 |

Missing-reference cases, separate from the table above:

| Cohort | Parties: matched/missing | Date: matched/missing | Law: matched/missing |
| --- | --- | --- | --- |
| Initial MVP | 0/0 | 0/0 | 0/0 |
| Earlier prompt | 0/0 | 2/2 | 4/4 |
| Revised prompt — regression | 1/1 | 1/1 | 3/3 |
| Revised prompt — first unseen set | 0/0 | 1/1 | 1/1 |
| Revised prompt — final unseen set | 0/0 | 0/0 | 8/8 |

## Final 20 unseen contracts

No extraction prompt, schema, or evaluator changes were made during this run. Selection used seed 20261017: four new filenames per targeted group (amendments, signature blocks, party scope, jurisdiction detail, missing/partial references), each at most 200,000 bytes. Filename novelty does not imply independence from companies or contract families seen previously.

- Completed: **20/20**, failed: **0**.
- Batch time: **247.2 seconds**.
- Recorded tokens: **253,027** (input 216,490; output 5,422; thinking 31,115).
- Evidence: **88/88** populated quotes found in source after whitespace normalization. This checks presence, not semantic correctness.
- Contracts with at least one mismatch/unscored field: **12/20**. The 15 flagged field comparisons were reviewed against source text and annotations.
- Four incomplete dates remain null and unscored. Two dates follow our stated/as-of convention while CUAD uses signature dates (FuelCell and Glu Amendment No. 1). No rules were changed to force these to match.
- Additional all-match spot checks included Arc Group, Bellring, GSV, Innoviva, King, Opera and ScanSource; this is not an independent exhaustive ground-truth audit.

[Validation manifest](data/validation_manifest.json)

## Earlier findings retained

- Apollo and BNL date failures were fixed in the revised-prompt regression run. Their current saved results are included; earlier failures remain documented in the linked baseline review.
- Netgear party comparison intentionally remains unchanged. Its amendment text includes INGRAM MICRO INC.; CUAD omits the suffix.
- The initial Cybergy sample retains the known Knowledge/Kowledge reference typo.
- Previously reviewed cases involving unknown template parties and affiliate scope remain review cases rather than fabricated names.
- Saved-output re-evaluation previously separated evaluator improvements from model improvements. This report reuses those saved final results; it does not run that re-evaluation again.

Historical JSON outputs and intermediate reviews remain local in `data/processed/` (excluded from Git). Their main findings are consolidated in this report.

## All tested contracts — index

| # | Contract | Cohort | Saved comparison outcome |
| ---: | --- | --- | --- |
| 1 | [CybergyHoldingsInc_20140520_10-Q_EX-10.27_8605784_EX-10.27_Affiliate Agreement.txt](#case-1) | Initial MVP | Needs review |
| 2 | [ArtaraTherapeuticsInc_20200110_8-K_EX-10.5_11943350_EX-10.5_License Agreement.txt](#case-2) | Earlier prompt | Needs review |
| 3 | [BLACKBOXSTOCKSINC_08_05_2014-EX-10.1-DISTRIBUTOR AGREEMENT.txt](#case-3) | Earlier prompt | All three fields match |
| 4 | [CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement2.txt](#case-4) | Earlier prompt | Needs review |
| 5 | [CORIOINC_07_20_2000-EX-10.5-LICENSE AND HOSTING AGREEMENT.txt](#case-5) | Earlier prompt | Needs review |
| 6 | [FUSIONPHARMACEUTICALSINC_06_05_2020-EX-10.17-Supply Agreement - FUSION.txt](#case-6) | Earlier prompt | Needs review |
| 7 | [GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement1.txt](#case-7) | Earlier prompt | Needs review |
| 8 | [INTELLIGENTHIGHWAYSOLUTIONS,INC_01_18_2018-EX-10.1-Strategic Alliance Agreement.txt](#case-8) | Earlier prompt | All three fields match |
| 9 | [IpassInc_20181203_8-K_EX-99.1_11445874_EX-99.1_Reseller Agreement.txt](#case-9) | Earlier prompt | All three fields match |
| 10 | [MPLXLP_06_17_2015-EX-10.1-TRANSPORTATION SERVICES AGREEMENT.txt](#case-10) | Earlier prompt | Needs review |
| 11 | [OASYSMOBILE,INC_07_05_2001-EX-10.17-OUTSOURCING AGREEMENT.txt](#case-11) | Earlier prompt | Needs review |
| 12 | [OMINTO,INC_03_29_2004-EX-10-RESELLER AGREEMENT.txt](#case-12) | Earlier prompt | All three fields match |
| 13 | [ParatekPharmaceuticalsInc_20170505_10-KA_EX-10.29_10323872_EX-10.29_Outsourcing Agreement.txt](#case-13) | Earlier prompt | All three fields match |
| 14 | [PFSFUNDS_06_26_2020-EX-99.H OTH MAT CONT-SERVICES AGREEMENT.txt](#case-14) | Earlier prompt | All three fields match |
| 15 | [RaeSystemsInc_20001114_10-Q_EX-10.57_2631790_EX-10.57_Co-Branding Agreement.txt](#case-15) | Earlier prompt | Needs review |
| 16 | [ReynoldsConsumerProductsInc_20200121_S-1A_EX-10.22_11948918_EX-10.22_Service Agreement.txt](#case-16) | Earlier prompt | Needs review |
| 17 | [SalesforcecomInc_20171122_10-Q_EX-10.1_10961535_EX-10.1_Reseller Agreement.txt](#case-17) | Earlier prompt | Needs review |
| 18 | [SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise Agreement1.txt](#case-18) | Earlier prompt | Needs review |
| 19 | [TICKETSCOMINC_06_22_1999-EX-10.22-SPONSORSHIP AGREEMENT.txt](#case-19) | Earlier prompt | Needs review |
| 20 | [TomOnlineInc_20060501_20-F_EX-4.46_749700_EX-4.46_Co-Branding Agreement.txt](#case-20) | Earlier prompt | Needs review |
| 21 | [UAGHINC_04_14_2004-EX-10.18-MAINTENANCE AGREEMENT.txt](#case-21) | Earlier prompt | All three fields match |
| 22 | [VnueInc_20150914_8-K_EX-10.1_9259571_EX-10.1_Promotion Agreement.txt](#case-22) | Earlier prompt | Needs review |
| 23 | [WESTERN COPPER - NON-COMPETITION AGREEMENT.txt](#case-23) | Earlier prompt | Needs review |
| 24 | [XinhuaSportsEntertainmentLtd_20070221_F-1_EX-99.4_645553_EX-99.4_Content License Agreement.txt](#case-24) | Earlier prompt | All three fields match |
| 25 | [ADUROBIOTECH,INC_06_02_2020-EX-10.7-CONSULTING AGREEMENT.txt](#case-25) | Revised prompt — regression | All three fields match |
| 26 | [Apollo Endosurgery - Manufacturing and Supply Agreement.txt](#case-26) | Revised prompt — regression | Needs review |
| 27 | [BNLFINANCIALCORP_03_30_2007-EX-10.8-OUTSOURCING AGREEMENT.txt](#case-27) | Revised prompt — regression | All three fields match |
| 28 | [GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement4.txt](#case-28) | Revised prompt — regression | All three fields match |
| 29 | [GRIDIRONBIONUTRIENTS,INC_02_05_2020-EX-10.3-SUPPLY AGREEMENT.txt](#case-29) | Revised prompt — regression | Needs review |
| 30 | [NETGEAR,INC_04_21_2003-EX-10.16- AMENDMENT #2 TO THE DISTRIBUTION AGREEMENT.txt](#case-30) | Revised prompt — regression | Needs review |
| 31 | [SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise Agreement3.txt](#case-31) | Revised prompt — regression | All three fields match |
| 32 | [UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Affiliate Agreement.txt](#case-32) | Revised prompt — regression | All three fields match |
| 33 | [VEONEER,INC_02_21_2020-EX-10.11-JOINT VENTURE AGREEMENT.txt](#case-33) | Revised prompt — regression | All three fields match |
| 34 | [ALLISONTRANSMISSIONHOLDINGSINC_12_15_2014-EX-99.1-COOPERATION AGREEMENT.txt](#case-34) | Revised prompt — first unseen set | Needs review |
| 35 | [BLUEROCKRESIDENTIALGROWTHREIT,INC_06_01_2016-EX-1.1-AGENCY AGREEMENT.txt](#case-35) | Revised prompt — first unseen set | Needs review |
| 36 | [EMERALDHEALTHTHERAPEUTICSINC_06_10_2020-EX-4.5-CONSULTING AGREEMENT - DR. GAETANO MORELLO N.D. INC..txt](#case-36) | Revised prompt — first unseen set | Needs review |
| 37 | [EuromediaHoldingsCorp_20070215_10SB12G_EX-10.B(01)_525118_EX-10.B(01)_Content License Agreement.txt](#case-37) | Revised prompt — first unseen set | Needs review |
| 38 | [INGEVITYCORP_05_16_2016-EX-10.5-INTELLECTUAL PROPERTY AGREEMENT.txt](#case-38) | Revised prompt — first unseen set | All three fields match |
| 39 | [N2KINC_10_16_1997-EX-10.16-SPONSORSHIP AGREEMENT.txt](#case-39) | Revised prompt — first unseen set | All three fields match |
| 40 | [PACIFICSYSTEMSCONTROLTECHNOLOGYINC_08_24_2000-EX-10.53-SPONSORSHIP AGREEMENT.txt](#case-40) | Revised prompt — first unseen set | Needs review |
| 41 | [PrecheckHealthServicesInc_20200320_8-K_EX-99.2_12070169_EX-99.2_Distributor Agreement.txt](#case-41) | Revised prompt — first unseen set | All three fields match |
| 42 | [RISEEDUCATIONCAYMANLTD_04_17_2020-EX-4.23-SERVICE AGREEMENT.txt](#case-42) | Revised prompt — first unseen set | Needs review |
| 43 | [SENMIAOTECHNOLOGYLTD_02_19_2019-EX-10.5-Collaboration Agreement.txt](#case-43) | Revised prompt — first unseen set | All three fields match |
| 44 | [ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorship Agreement.txt](#case-44) | Revised prompt — final unseen set | All three fields match |
| 45 | [BellringBrandsInc_20190920_S-1_EX-10.12_11817081_EX-10.12_Manufacturing Agreement2.txt](#case-45) | Revised prompt — final unseen set | All three fields match |
| 46 | [CHINARECYCLINGENERGYCORP_11_14_2013-EX-10.6-Cooperation Agreement.txt](#case-46) | Revised prompt — final unseen set | Needs review |
| 47 | [FuelcellEnergyInc_20191106_8-K_EX-10.1_11868007_EX-10.1_Development Agreement.txt](#case-47) | Revised prompt — final unseen set | Needs review |
| 48 | [GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement2.txt](#case-48) | Revised prompt — final unseen set | Needs review |
| 49 | [GSVINC_05_15_1998-EX-10-SPONSORSHIP AGREEMENT.txt](#case-49) | Revised prompt — final unseen set | All three fields match |
| 50 | [INNOVIVA,INC_08_07_2014-EX-10.1-COLLABORATION AGREEMENT.txt](#case-50) | Revised prompt — final unseen set | All three fields match |
| 51 | [KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMENT.txt](#case-51) | Revised prompt — final unseen set | All three fields match |
| 52 | [LegacyEducationAllianceInc_20141110_8-K_EX-10.9_8828866_EX-10.9_Endorsement Agreement.txt](#case-52) | Revised prompt — final unseen set | Needs review |
| 53 | [LIGHTBRIDGECORP_11_23_2015-EX-10.26-STRATEGIC ALLIANCE AGREEMENT.txt](#case-53) | Revised prompt — final unseen set | Needs review |
| 54 | [NEONSYSTEMSINC_03_01_1999-EX-10.5-DISTRIBUTOR AGREEMENT_Amendment.txt](#case-54) | Revised prompt — final unseen set | All three fields match |
| 55 | [OPERALTD_04_30_2020-EX-4.14-SERVICE AGREEMENT.txt](#case-55) | Revised prompt — final unseen set | All three fields match |
| 56 | [QBIOMEDINC_04_08_2020-EX-99.1-JOINT FILING AGREEMENT.txt](#case-56) | Revised prompt — final unseen set | Needs review |
| 57 | [ScansourceInc_20190822_10-K_EX-10.39_11793959_EX-10.39_Distributor Agreement.txt](#case-57) | Revised prompt — final unseen set | All three fields match |
| 58 | [SLINGERBAGINC_05_27_2020-EX-10.7-CONSULTING AGREEMENT.txt](#case-58) | Revised prompt — final unseen set | Needs review |
| 59 | [SMITHELECTRICVEHICLESCORP_04_04_2012-EX-10.26-FLEET MAINTENANCE AGREEMENT.txt](#case-59) | Revised prompt — final unseen set | Needs review |
| 60 | [SPARKLINGSPRINGWATERHOLDINGSLTD_07_03_2002-EX-10.13-SOFTWARE LICENSE AND MAINTENANCE AGREEMENT.txt](#case-60) | Revised prompt — final unseen set | Needs review |
| 61 | [VgrabCommunicationsInc_20200129_10-K_EX-10.33_11958828_EX-10.33_Development Agreement.txt](#case-61) | Revised prompt — final unseen set | Needs review |
| 62 | [VIVINT SOLAR, INC. - NON-COMPETITION AGREEMENT.txt](#case-62) | Revised prompt — final unseen set | Needs review |
| 63 | [XENCORINC_10_25_2013-EX-10.24-COLLABORATION AGREEMENT (3).txt](#case-63) | Revised prompt — final unseen set | Needs review |

## Per-contract results

Timing and tokens below belong to the selected saved output. They are not cumulative lifetime spend: earlier reruns and failed requests are not added, and unknown failed-request usage is not assumed to be zero. Historical evidence checks may not have been recorded; an earlier audit used case plus whitespace normalization, whereas current pipeline checks use whitespace normalization only.

<a id="case-1"></a>
### 1. CybergyHoldingsInc_20140520_10-Q_EX-10.27_8605784_EX-10.27_Affiliate Agreement.txt

**Cohort:** Initial MVP  
**Saved extraction started:** 13 Oct 2026 16:00:09 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.827 seconds · **Recorded tokens:** 8051

[Source TXT](data/raw/contracts/CybergyHoldingsInc_20140520_10-Q_EX-10.27_8605784_EX-10.27_Affiliate%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | BIRCH FIRST GLOBAL INVESTMENTS INC.<br>MOUNT KNOWLEDGE HOLDINGS INC. | Birch First Global Investments Inc.<br>Mount Kowledge Holdings Inc. | Mismatch |
| Agreement date | 2014-05-08 | 5/8/14 | Match |
| Governing law | State of Nevada | Nevada | Match |

**Evidence presence:** not recorded in this historical result.

**Review — parties (reference typo):** Reference spells Mount Knowledge as Mount Kowledge. Extraction matches the contract spelling; this is the original known annotation typo.

**Supporting quotes:**

- **parties:** This Marketing Affiliate Agreement (the "Agreement") is entered into this 8th day of May 2014, by and between BIRCH FIRST GLOBAL INVESTMENTS INC., a corporation incorporated in the U.S. Virgin Islands
- **parties:** MOUNT KNOWLEDGE HOLDINGS INC. and/or assigns, a corporation incorporated in the State of Nevada
- **agreement_date:** This Marketing Affiliate Agreement (the "Agreement") is entered into this 8th day of May 2014
- **governing_law:** This Agreement is accepted by Company in the State of Nevada and shall be governed by and construed in accordance with the laws thereof, which laws shall prevail in the event of any conflict.

<a id="case-2"></a>
### 2. ArtaraTherapeuticsInc_20200110_8-K_EX-10.5_11943350_EX-10.5_License Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:23:45 IST · **Model:** gemini-3.7-flash  
**Processing:** 10.255 seconds · **Recorded tokens:** 9744

[Source TXT](data/raw/contracts/validation_sample/ArtaraTherapeuticsInc_20200110_8-K_EX-10.5_11943350_EX-10.5_License%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | ArTara, Inc.<br>The University of Iowa | Artara Therapeutics, Inc.<br>The University of Iowa | Mismatch |
| Agreement date | 2018-11-28 | 11/28/18 | Match |
| Governing law | State of Iowa | Iowa | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Opening names ArTara, Inc. as extracted. Reference says Artara Therapeutics, Inc., which appears in the exhibit confidentiality notice; the contract-party evidence supports the extraction.

**Supporting quotes:**

- **parties:** This Sponsored Research and License Agreement (this "Agreement") is entered into on November 28, 2018 (the "Effective Date"), by and between ArTara, Inc.
- **parties:** and The University of Iowa, located at c/o Division of Sponsored Programs, 2 Gilmore Hall, Iowa City, IA 52242 ("University").
- **agreement_date:** This Sponsored Research and License Agreement (this "Agreement") is entered into on November 28, 2018 (the "Effective Date")
- **governing_law:** This Agreement shall be governed by the laws of the State of Iowa.

<a id="case-3"></a>
### 3. BLACKBOXSTOCKSINC_08_05_2014-EX-10.1-DISTRIBUTOR AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:23:55 IST · **Model:** gemini-3.7-flash  
**Processing:** 4.638 seconds · **Recorded tokens:** 4365

[Source TXT](data/raw/contracts/validation_sample/BLACKBOXSTOCKSINC_08_05_2014-EX-10.1-DISTRIBUTOR%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Snotarator LLC<br>SMSA Ballinger Acquisition Corp. | Snotarator LLC<br>SMSA Ballinger Acquisition Corp., | Match |
| Agreement date | 2013-08-01 | 8/1/13 | Match |
| Governing law | State of Texas | Texas | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** by and between Snotarator LLC, a Texas limited liability company, with its principal place of business located at 2591 Dallas Parkway, Suite 102, Frisco, Texas 75034 (the "Company")
- **parties:** SMSA Ballinger Acquisition Corp., a Nevada corporation, with offices at 12890 Hilltop Road, Argyle, Texas 76226 (the "Distributor").
- **agreement_date:** THIS AGREEMENT is made this 1st day of August, 2013
- **governing_law:** This Agreement shall be governed by the laws of the State of Texas.

<a id="case-4"></a>
### 4. CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance Agreement2.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:24:21 IST · **Model:** gemini-3.7-flash  
**Processing:** 4.467 seconds · **Recorded tokens:** 1372

[Source TXT](data/raw/contracts/validation_sample/CardlyticsInc_20180112_S-1_EX-10.16_11002987_EX-10.16_Maintenance%20Agreement2.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Bank of America, N.A. | Bank of America, N.A.<br>Supplier | Mismatch |
| Agreement date | null | null | Match |
| Governing law | null | null | Match |

**Earlier audit evidence presence:** 1/1 quotes found (case and whitespace normalized).

**Review — parties (schema/annotation scope):** An unfilled template names Bank of America and <<enter Company Name>> (Supplier). Model correctly avoids inventing a supplier legal name, while CUAD treats the role Supplier as a party. Decide how unknown named parties should be represented; the current full-legal-name schema has no explicit unknown-party representation.

**Supporting quotes:**

- **parties:** executed by and between Bank of America, N.A. ("Bank of America") and &lt;&lt;enter Company Name&gt;&gt; ("Supplier").

<a id="case-5"></a>
### 5. CORIOINC_07_20_2000-EX-10.5-LICENSE AND HOSTING AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:24:12 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.786 seconds · **Recorded tokens:** 13458

[Source TXT](data/raw/contracts/validation_sample/CORIOINC_07_20_2000-EX-10.5-LICENSE%20AND%20HOSTING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Corio Inc.<br>Commerce One, Inc. | Corio Inc.<br>Commerce One, Inc. | Match |
| Agreement date | 1999-10-29 | 10/29/99 | Match |
| Governing law | State of California, USA | California | Mismatch |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — governing_law (reference/evaluator):** Source explicitly specifies State of California, USA. Extraction preserves USA while reference says California. Same jurisdiction; evaluator only removes State of and cannot handle the added country.

**Supporting quotes:**

- **parties:** This License and Hosting Agreement (the "AGREEMENT") is made and entered into as of October 29, 1999 ("EFFECTIVE DATE") by and between Corio Inc., a Delaware corporation
- **parties:** Commerce One, Inc., a Delaware corporation having its principal place of business at 1600 Rivera Avenue, Walnut Creek, CA 94596 ("COMMERCE ONE").
- **agreement_date:** This License and Hosting Agreement (the "AGREEMENT") is made and entered into as of October 29, 1999 ("EFFECTIVE DATE")
- **governing_law:** This Agreement shall be governed by the laws of the State of California, USA, excluding conflict of laws provisions and excluding the 1980 United Nations Convention on Contracts for the International Sale of Goods.

<a id="case-6"></a>
### 6. FUSIONPHARMACEUTICALSINC_06_05_2020-EX-10.17-Supply Agreement - FUSION.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:24:26 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.97 seconds · **Recorded tokens:** 10033

[Source TXT](data/raw/contracts/validation_sample/FUSIONPHARMACEUTICALSINC_06_05_2020-EX-10.17-Supply%20Agreement%20-%20FUSION.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Centre for Probe Development and Commercialization<br>FUSION Pharmaceuticals Inc. | Centre for Probe Development and Commercialization<br>FUSION Pharmaceuticals Inc.<br>(together "Parties", each a "Party") | Mismatch |
| Agreement date | null | null | Match |
| Governing law | null | null | Match |

**Earlier audit evidence presence:** 2/2 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Both extracted organizations match the opening. CUAD adds a collective Parties/Party phrase as a third list entry; it is not another organization.

**Supporting quotes:**

- **parties:** SUPPLY AGREEMENT ("Supply Agreement") effective as of the date of last signing ("Effective Date") between Centre for Probe Development and Commercialization, a not-for-profit research and services institution with offices located at McMaster University, Nuclear Research Building, 1280 Main Street West, Hamilton, Ontario, Canada, L8S 4K1, ("CPDC")
- **parties:** FUSION Pharmaceuticals Inc. ("FUSION"), having a place of business at 270 Longwood Road South, Hamilton, Ontario, Canada, L8P 0A6, (together the "Parties" each a "Party").

<a id="case-7"></a>
### 7. GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement1.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:24:35 IST · **Model:** gemini-3.7-flash  
**Processing:** 19.067 seconds · **Recorded tokens:** 27070

[Source TXT](data/raw/contracts/validation_sample/GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content%20License%20Agreement1.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | TWENTIETH CENTURY FOX LICENSING &amp; MERCHANDISING, a division of Fox Entertainment Group, Inc.<br>Sorrent, Inc. | Twentieth Century Fox Licensing &amp; Merchandising<br>Sorrent, Inc | Mismatch |
| Agreement date | 2004-12-16 | 12/16/04 | Match |
| Governing law | State of California | California | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Extraction identifies the same two named contracting parties but retains the source's division-of-Fox-Entertainment-Group qualifier. CUAD omits that qualifier. This is a representation mismatch, not an unidentified counterparty.

**Supporting quotes:**

- **parties:** This License Agreement (this "Agreement") is entered into effective as of December 16, 2004, (the "Effective Date") by and between TWENTIETH CENTURY FOX LICENSING &amp; MERCHANDISING, a division of Fox Entertainment Group, Inc. ("Fox"), as Administrator for Twentieth Century Fox Film Corporation ("Trademark Licensor"), and Sorrent, Inc. ("Licensee").
- **parties:** This License Agreement (this "Agreement") is entered into effective as of December 16, 2004, (the "Effective Date") by and between TWENTIETH CENTURY FOX LICENSING &amp; MERCHANDISING, a division of Fox Entertainment Group, Inc. ("Fox"), as Administrator for Twentieth Century Fox Film Corporation ("Trademark Licensor"), and Sorrent, Inc. ("Licensee").
- **agreement_date:** This License Agreement (this "Agreement") is entered into effective as of December 16, 2004, (the "Effective Date")
- **governing_law:** This Agreement shall be construed in accordance with the laws of the State of California applicable to agreements executed and to be wholly performed therein.

<a id="case-8"></a>
### 8. INTELLIGENTHIGHWAYSOLUTIONS,INC_01_18_2018-EX-10.1-Strategic Alliance Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:24:54 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.39 seconds · **Recorded tokens:** 2986

[Source TXT](data/raw/contracts/validation_sample/INTELLIGENTHIGHWAYSOLUTIONS%2CINC_01_18_2018-EX-10.1-Strategic%20Alliance%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Bravatek Solutions, Inc.<br>Fazync LLC | Bravatek Solutions, Inc.<br>Fazync LLC | Match |
| Agreement date | 2018-01-10 | 1/10/18 | Match |
| Governing law | State of Texas | Texas | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** This agreement is made and entered into this 10th day of January, 2018 by and between Bravatek Solutions, Inc., a corporation organized under the laws of the State of Colorado, ("Bravatek")
- **parties:** Fazync LLC, a limited liability company organized under the laws of the State of Colorado with an address at 2376 Gold River Drive, Rancho Cordova, CA 95670 ("Fazync").
- **agreement_date:** This agreement is made and entered into this 10th day of January, 2018
- **governing_law:** This Agreement is entered into in the State of Texas and shall be interpreted according to the laws of the State of Texas.

<a id="case-9"></a>
### 9. IpassInc_20181203_8-K_EX-99.1_11445874_EX-99.1_Reseller Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:25:01 IST · **Model:** gemini-3.7-flash  
**Processing:** 57.443 seconds · **Recorded tokens:** 25005

[Source TXT](data/raw/contracts/validation_sample/IpassInc_20181203_8-K_EX-99.1_11445874_EX-99.1_Reseller%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | IPASS INC.<br>Pareteum Corporation | IPASS INC.<br>Pareteum Corporation | Match |
| Agreement date | 2018-04-25 | 4/25/18 | Match |
| Governing law | California | California | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** IPASS INC., having a principal place of business at 3800 Bridge Parkway, Redwood Shores, CA 94065 ("iPass")
- **parties:** Pareteum Corporation, having a principal business address at 100 Park Avenue, Suite 1600, New York City, New York 10017 ("Channel Partner")
- **agreement_date:** IN WITNESS WHEREOF, the parties have executed this Agreement as of the Effective Date. Channel Partner: iPass Inc.: By: /s/ Victor A. Bozzo By: /s/ Christine Gardner Victor A. Bozzo Christine Gardner Printed Name Printed Name Chief Executive Officer VP Finance Title Title 4/24/2018 04/25/2018 Date Date
- **governing_law:** The laws of California shall govern the construction and enforceability of the Agreement.

<a id="case-10"></a>
### 10. MPLXLP_06_17_2015-EX-10.1-TRANSPORTATION SERVICES AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:25:58 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.216 seconds · **Recorded tokens:** 13021

[Source TXT](data/raw/contracts/validation_sample/MPLXLP_06_17_2015-EX-10.1-TRANSPORTATION%20SERVICES%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Marathon Petroleum Company LP<br>Marathon Pipe Line LLC | Marathon Petroleum Company LP<br>Marathon Pipe Line LLC<br>Marathon Petroleum Company LP and Marathon Pipe Line LLC (jointly as "Parties" and individually as a "Party") | Mismatch |
| Agreement date | 2015-06-11 | 6/11/15 | Match |
| Governing law | the State of Ohio | Ohio | Mismatch |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Both extracted companies match the opening; CUAD adds a combined joint-Parties phrase as a third party.

**Review — governing_law (reference/evaluator):** Source specifies laws of the State of Ohio. Extraction the State of Ohio and reference Ohio identify the same jurisdiction; normalizer strips state of only when not preceded by the.

**Supporting quotes:**

- **parties:** THIS TRANSPORTATION SERVICES AGREEMENT (this "Agreement") is dated as of June 11, 2015, by and between Marathon Petroleum Company LP ("Shipper") and Marathon Pipe Line LLC, a Delaware limited liability company ("MPL"), both referred to jointly as the "Parties" and each individually as a "Party".
- **parties:** THIS TRANSPORTATION SERVICES AGREEMENT (this "Agreement") is dated as of June 11, 2015, by and between Marathon Petroleum Company LP ("Shipper") and Marathon Pipe Line LLC, a Delaware limited liability company ("MPL"), both referred to jointly as the "Parties" and each individually as a "Party".
- **agreement_date:** THIS TRANSPORTATION SERVICES AGREEMENT (this "Agreement") is dated as of June 11, 2015
- **governing_law:** This Agreement shall be construed and interpreted in accordance with the laws of the State of Ohio, without recourse to any principles of law governing conflicts of law, which might otherwise be applicable.

<a id="case-11"></a>
### 11. OASYSMOBILE,INC_07_05_2001-EX-10.17-OUTSOURCING AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:06 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.967 seconds · **Recorded tokens:** 13802

[Source TXT](data/raw/contracts/validation_sample/OASYSMOBILE%2CINC_07_05_2001-EX-10.17-OUTSOURCING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | E.PIPHANY, INC.<br>HIGH SPEED NET SOLUTIONS, INC. | E.PIPHANY, INC.<br>HIGH SPEED NET SOLUTIONS, INC. | Match |
| Agreement date | 2000-07-31 | 07/31/2000; 07/[]/2000 | Unscored — review |
| Governing law | the State of California | California | Mismatch |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — agreement_date (reference/evaluator):** Opening explicitly entered into July 31, 2000, as extracted. Exhibit A order-form template refers to July __, 2000. CUAD stores both as 07/31/2000; 07/[]/2000, unsupported by current scalar two-digit-year parser. Review result supports July 31 for main agreement.

**Review — governing_law (reference/evaluator):** Source specifies laws of the State of California. Extraction the State of California and reference California agree semantically; leading the defeats the simple normalizer.

**Supporting quotes:**

- **parties:** This ASP and Outsourcing Agreement ("Agreement") is entered into as of this 31 day of July, 2000 ("Effective Date") by and between E.PIPHANY, INC., a Delaware corporation ("E.piphany")
- **parties:** HIGH SPEED NET SOLUTIONS, INC. ("HSNS"), whose principal place of business is 434 Fayetteville Street, St. Suite 2120, Raleigh, NC 27601.
- **agreement_date:** This ASP and Outsourcing Agreement ("Agreement") is entered into as of this 31 day of July, 2000 ("Effective Date")
- **governing_law:** This Agreement, and all matters arising out of or relating to this Agreement, shall be governed by the laws of the State of California.

<a id="case-12"></a>
### 12. OMINTO,INC_03_29_2004-EX-10-RESELLER AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:12 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.743 seconds · **Recorded tokens:** 7345

[Source TXT](data/raw/contracts/validation_sample/OMINTO%2CINC_03_29_2004-EX-10-RESELLER%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | MediaNet Group Technologies, Inc.<br>International Direct Response, Inc. | MediaNet Group Technologies, Inc.<br>International Direct Response, Inc. | Match |
| Agreement date | 2004-03-19 | 3/19/04 | Match |
| Governing law | State of Florida | Florida | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** MediaNet Group Technologies, Inc., a Nevada corporation having an address at 5100 W. Copans Road Suite 710 Margate, FL 33063 USA ("MEDIANET GROUP TECHNOLOGIES")
- **parties:** International Direct Response, Inc., a Pennsylvania Corporation, having an address at 1125 Lancaster Avenue, Berwyn, PA 19312("RESELLER")
- **agreement_date:** THIS AGREEMENT (the "AGREEMENT") entered into as of the 19 day of March, 2004
- **governing_law:** The laws of the State of Florida shall govern this Agreement, without reference to conflicts of law provisions.

<a id="case-13"></a>
### 13. ParatekPharmaceuticalsInc_20170505_10-KA_EX-10.29_10323872_EX-10.29_Outsourcing Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:26 IST · **Model:** gemini-3.7-flash  
**Processing:** 10.51 seconds · **Recorded tokens:** 26615

[Source TXT](data/raw/contracts/validation_sample/ParatekPharmaceuticalsInc_20170505_10-KA_EX-10.29_10323872_EX-10.29_Outsourcing%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Paratek Pharmaceuticals, Inc.<br>CARBOGEN AMCIS AG | Paratek Pharmaceuticals, Inc.<br>CARBOGEN AMCIS AG | Match |
| Agreement date | 2016-12-30 | 12/30/16 | Match |
| Governing law | null | null | Match |

**Earlier audit evidence presence:** 3/3 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** Paratek Pharmaceuticals, Inc., a company having a place of business at 75 Park Plaza, 4t h Floor, Boston, MA 02116, USA ("Customer")
- **parties:** CARBOGEN AMCIS AG, a company having a place of business at Hauptstrasse 171, CH 4416 Bubendorf, Switzerland ("Supplier" and, collectively with Customer, the "Parties", and each, a "Party).
- **agreement_date:** THIS AGREEMENT (this "Agreement"), dated December 30, 2016 (the "Effective Date"), is BETWEEN:

<a id="case-14"></a>
### 14. PFSFUNDS_06_26_2020-EX-99.H OTH MAT CONT-SERVICES AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:20 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.466 seconds · **Recorded tokens:** 3883

[Source TXT](data/raw/contracts/validation_sample/PFSFUNDS_06_26_2020-EX-99.H%20OTH%20MAT%20CONT-SERVICES%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | PFS Funds<br>Potomac Fund Management, Inc. | PFS Funds<br>Potomac Fund Management, Inc. | Match |
| Agreement date | 2020-06-24 | 6/24/20 | Match |
| Governing law | State of Massachusetts | Massachusetts | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** between PFS Funds (the "Trust"), a Massachusetts business trust, and Potomac Fund Management, Inc. (the "Adviser"), a Florida Corporation.
- **parties:** between PFS Funds (the "Trust"), a Massachusetts business trust, and Potomac Fund Management, Inc. (the "Adviser"), a Florida Corporation.
- **agreement_date:** AGREEMENT dated as of June 24, 2020, between PFS Funds (the "Trust"), a Massachusetts business trust, and Potomac Fund Management, Inc. (the "Adviser"), a Florida Corporation.
- **governing_law:** This Agreement shall be construed and enforced in accordance with and governed by the laws of the State of Massachusetts.

<a id="case-15"></a>
### 15. RaeSystemsInc_20001114_10-Q_EX-10.57_2631790_EX-10.57_Co-Branding Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:36 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.126 seconds · **Recorded tokens:** 12140

[Source TXT](data/raw/contracts/validation_sample/RaeSystemsInc_20001114_10-Q_EX-10.57_2631790_EX-10.57_Co-Branding%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | NETTAXI Online Communities, Inc.<br>Solutions Media, Inc., dba SpinRecords.com | NETTAXI Online Communities, Inc.<br>Solutions Media, Inc.(dba SpinRecords.com, "SpinRecords.com" or "Client") | Mismatch |
| Agreement date | 1999-11-05 | 11/5/99 | Match |
| Governing law | State of California and the United States | California | Mismatch |

**Earlier audit evidence presence:** 3/4 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Extraction preserves Solutions Media dba SpinRecords.com as in opening. Reference places the dba and aliases in a parenthetical, which evaluator retains because it starts with dba. Same entities, incompatible representation.

**Review — governing_law (reference/evaluator):** Source explicitly includes laws of both California and the United States; extraction preserves both while reference omits United States. Do not blindly remove federal law to force a match.

**Supporting quotes:**

- **parties:** NETTAXI Online Communities, Inc., a Delaware corporation with principal offices at 2165 S. Bascom Avenue, Campbell, California 95008 ("NETTAXI")
- **parties:** Solutions Media, Inc., dba SpinRecords.com a Delaware Corporation, with offices at 11440 West Barnardo Ct., Suite 170, San Diego, CA 32127 ("SpinRecords.com" or "Client")
- **agreement_date:** This CO-BRANDING AGREEMENT (the "Agreement") is made and entered into as of Nov  5,  1999
- **governing_law:** This Agreement and any action related thereto shall be governed, controlled, interpreted and defined by and under the laws of the State of California and the United States, without regard to the conflicts of laws provisions thereof.

<a id="case-16"></a>
### 16. ReynoldsConsumerProductsInc_20200121_S-1A_EX-10.22_11948918_EX-10.22_Service Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:44 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.317 seconds · **Recorded tokens:** 25861

[Source TXT](data/raw/contracts/validation_sample/ReynoldsConsumerProductsInc_20200121_S-1A_EX-10.22_11948918_EX-10.22_Service%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Reynolds Group Holdings Inc.<br>Reynolds Consumer Products Inc. | Reynolds Group Holdings Inc.<br>Reynolds Consumer Products Inc.<br>Each Party or any of its Affiliates providing services hereunder<br>each Party or any of its Affiliates receiving services hereunder | Mismatch |
| Agreement date | null | []/[]/2020 | Unscored — review |
| Governing law | State of Illinois | Illinois | Match |

**Earlier audit evidence presence:** 3/3 quotes found (case and whitespace normalized).

**Review — parties (schema/annotation scope):** Opening identifies the two extracted legal entities. CUAD also includes generic provider/recipient descriptions referring to parties and affiliates. No additional named entity can be recovered from those role descriptions.

**Review — agreement_date (reference/evaluator):** Opening date is [bullet], 2020, with no month/day. Extraction null is appropriate for the complete-date schema; reference []/[]/2020 cannot be scored as a complete date.

**Supporting quotes:**

- **parties:** between Reynolds Group Holdings Inc., a Delaware corporation ("RGHI"), and Reynolds Consumer Products Inc., a Delaware corporation, (the "Company" or "RCP").
- **parties:** between Reynolds Group Holdings Inc., a Delaware corporation ("RGHI"), and Reynolds Consumer Products Inc., a Delaware corporation, (the "Company" or "RCP").
- **governing_law:** This Agreement shall be governed in all respects, including as to validity, interpretation and effect, by the Laws of the State of Illinois, without giving effect to its principles or rules of conflict of laws

<a id="case-17"></a>
### 17. SalesforcecomInc_20171122_10-Q_EX-10.1_10961535_EX-10.1_Reseller Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:51 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.478 seconds · **Recorded tokens:** 1855

[Source TXT](data/raw/contracts/validation_sample/SalesforcecomInc_20171122_10-Q_EX-10.1_10961535_EX-10.1_Reseller%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Salesforce.org<br>salesforce.com, inc. | salesforce.com, inc.<br>Salesforce.org | Match |
| Agreement date | null | []/[]/[] | Unscored — review |
| Governing law | null | null | Match |

**Earlier audit evidence presence:** 2/2 quotes found (case and whitespace normalized).

**Review — agreement_date (reference/evaluator):** Reference []/[]/[] is a blank placeholder and its evidence list is empty. Extraction null does not invent a date. Parser correctly flags the placeholder for review rather than treating it as an ordinary date.

**Supporting quotes:**

- **parties:** Reseller Full Legal Name Salesforce.org, a nonprofit public benefit corporation having its principal place of business at 50 Fremont Street, Suite 300, San Francisco, California 94105
- **parties:** This Form of Sub-Reseller Agreement (this "Sub-Reseller Agreement") is made and entered in by and between salesforce.com, inc., a Delaware corporation having its principal place of business at The Landmark @ One Market, Suite 300, San Francisco, California 94105

<a id="case-18"></a>
### 18. SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise Agreement1.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:26:57 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.786 seconds · **Recorded tokens:** 31115

[Source TXT](data/raw/contracts/validation_sample/SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise%20Agreement1.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Kiosk Concepts, Inc.<br>The Grilled Cheese Truck, Inc. | Kiosk Concepts Inc.<br>The Grilled Cheese Truck, Inc. | Match |
| Agreement date | null | []/[]/2015 | Unscored — review |
| Governing law | State of New York | New York | Match |

**Earlier audit evidence presence:** 3/3 quotes found (case and whitespace normalized).

**Review — agreement_date (reference/evaluator):** Main agreement date has blank day/month and only year 2015. Null is appropriate for complete-date schema; reference []/[]/2015 is unsupported and unscored.

**Supporting quotes:**

- **parties:** AGREEMENT made as of the _____ day of __________________, 2015 (the "Effective Date") by and between Kiosk Concepts, Inc., a New York corporation having its principal place of business at 1110 South Avenue, Staten Island, New York 10314
- **parties:** and The Grilled Cheese Truck, Inc., a Nevada corporation having its principal address at 151 North Nob Hill Road, Suite 321, Fort Lauderdale, FL 33324
- **governing_law:** This Agreement shall be interpreted and construed under the laws of the State of New York.

<a id="case-19"></a>
### 19. TICKETSCOMINC_06_22_1999-EX-10.22-SPONSORSHIP AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:04 IST · **Model:** gemini-3.7-flash  
**Processing:** 4.964 seconds · **Recorded tokens:** 2618

[Source TXT](data/raw/contracts/validation_sample/TICKETSCOMINC_06_22_1999-EX-10.22-SPONSORSHIP%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Tickets.com, Inc.<br>MP3.com, Inc. | Tickets.com Inc. "Tickets"<br>MP3.com Inc. "MP3.com" | Mismatch |
| Agreement date | 1999-02-17 | 2/17/99 | Match |
| Governing law | State of California | California | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Both extracted full legal names match the opening. Reference appends aliases Tickets and MP3.com in quotes without parentheses, which current alias-cleaning rule does not remove.

**Supporting quotes:**

- **parties:** by and between Tickets.com, Inc., a Delaware corporation, located at 4061 Glencoe Ave., Marina del Rey, CA 90292 ("Tickets")
- **parties:** MP3.com, Inc., having an address at P.O. Box 910091, San Diego, CA 92191-0091 ("MP3.com").
- **agreement_date:** This Sponsorship Agreement ("Agreement") is made an entered into on February 17, 1999 ("Effective Date")
- **governing_law:** This Agreement shall be governed by and construed in accordance with the laws of the State of California without reference to conflict of law principles thereof.

<a id="case-20"></a>
### 20. TomOnlineInc_20060501_20-F_EX-4.46_749700_EX-4.46_Co-Branding Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:09 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.621 seconds · **Recorded tokens:** 25274

[Source TXT](data/raw/contracts/validation_sample/TomOnlineInc_20060501_20-F_EX-4.46_749700_EX-4.46_Co-Branding%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Skype Communications, S.A.<br>Skype Technologies, S.A.<br>TOM Online (BVI) Limited<br>TOM Online Inc.<br>Tel-Online Limited | Skype Communications, S.A.<br>Skype Technologies, S.A.<br>TOM Online (BVI) limited<br>TOM Online Inc.<br>Tel Online Limited . Skype, Online BVI and the Company<br>Skype, Online BVI, the Company, Skype Holding and Tom Holding | Mismatch |
| Agreement date | 2005-08-22 | 8/22/05 | Match |
| Governing law | England and Wales | England, United Kingdom; Wales, United Kingdom | Mismatch |

**Earlier audit evidence presence:** 7/7 quotes found (case and whitespace normalized).

**Review — parties (reference/evaluator):** Extraction includes all five entities in the opening enumeration. Reference combines one name with collective text and adds an extra alias-list entry. Legal-name parentheses (BVI) are correctly preserved.

**Review — governing_law (reference/evaluator):** Source explicitly says laws of England and Wales, as extracted. Reference expands this into England, United Kingdom; Wales, United Kingdom; the string comparator cannot recognize that representation.

**Supporting quotes:**

- **parties:** by and among (a) Skype Communications, S.A. ("Skype"), a limited company (société anonyme) incorporated in Luxembourg
- **parties:** (b) Skype Technologies, S.A. ("Skype Holding"), a limited company (société anonyme) incorporated in Luxembourg
- **parties:** (c) TOM Online (BVI) Limited ("Online BVI"), a company incorporated in the British Virgin Islands with limited liability
- **parties:** (d) TOM Online Inc. ("Tom Holding"), a company incorporated in the Cayman Islands with limited liability
- **parties:** (e) Tel-Online Limited ("Company"), a company incorporated in the Cayman Islands
- **agreement_date:** THIS CO-BRANDING AGREEMENT (this "Agreement"), entered into on the 22nd day of August 2005
- **governing_law:** This Agreement will be governed by and construed in accordance with the laws of England and Wales, without regard to conflict of laws principles.

<a id="case-21"></a>
### 21. UAGHINC_04_14_2004-EX-10.18-MAINTENANCE AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:18 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.256 seconds · **Recorded tokens:** 4698

[Source TXT](data/raw/contracts/validation_sample/UAGHINC_04_14_2004-EX-10.18-MAINTENANCE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Universal Access, Inc.<br>CityNet Telecommunications, Inc. | Universal Access, Inc.<br>CityNet Telecommunications, Inc. | Match |
| Agreement date | 2003-07-23 | 7/23/03 | Match |
| Governing law | State of Delaware | Delaware | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** MAINTENANCE AGREEMENT (this "Agreement"), dated as of July 23, 2003, made by Universal Access, Inc., a corporation organized and existing under the laws of the State of Delaware (the "Company")
- **parties:** CityNet Telecommunications, Inc., a corporation organized and existing under the laws of the State of Delaware (the "Provider").
- **agreement_date:** MAINTENANCE AGREEMENT (this "Agreement"), dated as of July 23, 2003
- **governing_law:** THIS AGREEMENT AND THE RIGHTS AND OBLIGATIONS OF THE PARTIES HEREUNDER SHALL BE CONSTRUED ACCORDING TO AND GOVERNED BY THE SUBSTANTIVE LAWS OF THE STATE OF DELAWARE

<a id="case-22"></a>
### 22. VnueInc_20150914_8-K_EX-10.1_9259571_EX-10.1_Promotion Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:24 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.5 seconds · **Recorded tokens:** 3493

[Source TXT](data/raw/contracts/validation_sample/VnueInc_20150914_8-K_EX-10.1_9259571_EX-10.1_Promotion%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | BookingEntertainment.com<br>VNUE, Inc. | BookingEntertainment.com<br>VNUE, Inc. | Match |
| Agreement date | 2015-09-10 | 9/10/15 | Match |
| Governing law | the State of Nevada | Nevada | Mismatch |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — governing_law (reference/evaluator):** Source specifies laws of the State of Nevada. Extraction the State of Nevada and reference Nevada refer to the same jurisdiction; the normalizer does not strip the leading the.

**Supporting quotes:**

- **parties:** between BookingEntertainment.com ("Promoter") of 275 Madison Avenue, 6t h Floor, New York, NY 10016
- **parties:** VNUE, Inc., ("VNUE"), a Nevada corporation quoted on the OTCMarkets, with offices at 104 West 29th Street 11th Floor, New York, NY 10001.
- **agreement_date:** This Promotion Agreement ("Agreement") is entered into effective September 10, 2015
- **governing_law:** This Agreement shall be governed by and construed in accordance with the laws of the State of Nevada without giving effect to choice of law doctrine.

<a id="case-23"></a>
### 23. WESTERN COPPER - NON-COMPETITION AGREEMENT.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:31 IST · **Model:** gemini-3.7-flash  
**Processing:** 4.893 seconds · **Recorded tokens:** 4503

[Source TXT](data/raw/contracts/validation_sample/WESTERN%20COPPER%20-%20NON-COMPETITION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | GLAMIS GOLD LTD.<br>WESTERN COPPER CORPORATION | Glamis Gold Ltd. and all of its subsidiaries and other Affiliates<br>Western Copper Corporation and all of its subsidiaries and other Affiliates | Mismatch |
| Agreement date | 2006-05-03 | 5/3/06 | Match |
| Governing law | Province of British Columbia | British Columbia | Mismatch |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Review — parties (schema/annotation scope):** Extraction identifies the two named signatories. Section 1.3 expressly expands the names to include subsidiaries and other Affiliates; CUAD includes that scope in each answer. Named-party extraction is supported, but affiliate scope is not represented. Treat this as a scope limitation requiring a policy decision, not merely punctuation.

**Review — governing_law (reference/evaluator):** Source specifies laws of the Province of British Columbia. Extraction preserves Province of while reference does not. Same jurisdiction; current normalizer only strips State of.

**Supporting quotes:**

- **parties:** GLAMIS GOLD LTD., a company incorporated under the laws  of the Province of British Columbia, having an office at 310-5190  Neil Road, Reno, Nevada 89502
- **parties:** WESTERN COPPER CORPORATION, a company  incorporated under the laws of the Province of British Columbia,  having an office at 2050-1111 West Georgia Street, Vancouver.  B.C. V6E 4M3
- **agreement_date:** THIS AGREEMENT is dated May 3,2006.
- **governing_law:** This Agreement will be governed exclusively by and construed in accordance  with the laws of the Province of British Columbia, and the parties attorn to the exclusive  jurisdiction of the Courts of British Columbia.

<a id="case-24"></a>
### 24. XinhuaSportsEntertainmentLtd_20070221_F-1_EX-99.4_645553_EX-99.4_Content License Agreement.txt

**Cohort:** Earlier prompt  
**Saved extraction started:** 15 Oct 2026 10:27:36 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.827 seconds · **Recorded tokens:** 4937

[Source TXT](data/raw/contracts/validation_sample/XinhuaSportsEntertainmentLtd_20070221_F-1_EX-99.4_645553_EX-99.4_Content%20License%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | CHINA ECONOMIC INFORMATION SERVICE OF XINHUA NEWS AGENCY<br>XINHUA FINANCIAL NETWORK LIMITED | CHINA ECONOMIC INFORMATION SERVICE OF XINHUA NEWS AGENCY<br>XINHUA FINANCIAL NETWORK LIMITED | Match |
| Agreement date | 2001-12-15 | 12/15/01 | Match |
| Governing law | Hong Kong | Hong Kong | Match |

**Earlier audit evidence presence:** 4/4 quotes found (case and whitespace normalized).

**Supporting quotes:**

- **parties:** CHINA ECONOMIC INFORMATION SERVICE OF XINHUA NEWS AGENCY, the organisation within the Xinhua News Agency that is responsible for news and information operations and business, registered in the People's Republic of China with offices at 57 Xuanwumen Xidajie, Beijing, the People's Republic of China ( "CEIS")
- **parties:** XINHUA FINANCIAL NETWORK LIMITED, a company incorporated in Hong Kong whose registered office is at Room 2003-4, Vicwood Plaza, 199 Des Voeux Road Central, Hong Kong ("XFN")
- **agreement_date:** THIS AGREEMENT is made the 15th day of December 2001.
- **governing_law:** This Agreement is governed by and shall be construed in accordance with the laws of Hong Kong

<a id="case-25"></a>
### 25. ADUROBIOTECH,INC_06_02_2020-EX-10.7-CONSULTING AGREEMENT.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:33:16 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.903 seconds · **Recorded tokens:** 3951

[Source TXT](data/raw/contracts/batch_sample/ADUROBIOTECH%2CINC_06_02_2020-EX-10.7-CONSULTING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Aduro Biotech, Inc.<br>IREYA B.V | Aduro Biotech, Inc<br>IREYA B.V | Match |
| Agreement date | 2020-06-01 | 6/1/20 | Match |
| Governing law | State of California | California | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Aduro Biotech, Inc ("Aduro"); IREYA B.V ("Consultant")

**Supporting quotes:**

- **parties:** Aduro Biotech, Inc., with a place of business at 740 Heinz Avenue, Berkeley, CA 94710 ("Aduro")
- **parties:** IREYA B.V having an address at Staalwijkstraat 16, 2313 XR Leiden, the Netherlands, represented by Andrea van Elsas, ("Consultant")
- **agreement_date:** this Consulting Agreement ("Agreement") dated June 1, 2020
- **governing_law:** This Agreement shall be construed and enforced in accordance with the laws of the State of California, without regard to the conflict of law principles of California or any other jurisdiction.

<a id="case-26"></a>
### 26. Apollo Endosurgery - Manufacturing and Supply Agreement.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:41:15 IST · **Model:** gemini-3.7-flash  
**Processing:** 56.446 seconds · **Recorded tokens:** 11940

[Source TXT](data/raw/contracts/validation_sample/Apollo%20Endosurgery%20-%20Manufacturing%20and%20Supply%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Apollo Endosurgery, Inc.<br>Establishment Labs, S.A | Apollo Endosurgery<br>Establishment Labs, S.A | Mismatch |
| Agreement date | 2014-12-05 | 12/5/14 | Match |
| Governing law | State of Texas | Texas | Match |

**Date basis:** `defined_date`.

**Evidence presence:** 6/6 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** Parties are supported by the opening/signature block; reference omits Apollo Inc. The date now resolves the explicitly linked Effective Date definition to December 5, 2014.

**Original CUAD parties answer:** Apollo Endosurgery ("APOLLO"); Establishment Labs, S.A ("ESTABLISHMENT"); Apollo and Establishment shall hereinafter be individually referred to as a "Party" and collectively as the "Parties"

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** (1) Apollo Endosurgery, Delaware corporation having offices at 1120 S Capital of Texas Highway #300, Austin, TX 78746 ("APOLLO")
- **parties:** Apollo Endosurgery, Inc.
- **parties:** (2) Establishment Labs, S.A a corporation organized under the laws of Costa Rica and having a principal place of business at Coyol Free Zone, B15, Alajuela, 20113, Costa Rica ("ESTABLISHMENT")
- **agreement_date:** This Manufacturing and Supply Agreement (this "Agreement") is entered into as of the Effective Date (as defined below)
- **agreement_date:** 1.5"Effective Date" shall mean December 5, 2014.
- **governing_law:** Notwithstanding its place of execution or performance, this Agreement shall be governed by and construed in accordance with the laws of the State of Texas, irrespective of its laws regarding choice or conflict of laws.

<a id="case-27"></a>
### 27. BNLFINANCIALCORP_03_30_2007-EX-10.8-OUTSOURCING AGREEMENT.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:42:12 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.973 seconds · **Recorded tokens:** 10027

[Source TXT](data/raw/contracts/validation_sample/BNLFINANCIALCORP_03_30_2007-EX-10.8-OUTSOURCING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Virtual Item Processing Systems, Inc.<br>Brokers National Life Assurance Company | Virtual Item Processing Systems, Inc.<br>Brokers National Life Assurance Company | Match |
| Agreement date | 2006-05-01 | 5/1/06 | Match |
| Governing law | State of Oklahoma | Oklahoma | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Virtual Item Processing Systems, Inc. ("VIP"); Brokers National Life Assurance Company ("BNL")

**Supporting quotes:**

- **parties:** This Outsourcing Agreement (" Agreement") is executed as of this 1 st  day of May 2006, by and between Virtual Item Processing Systems, Inc. ("VIP"), with its principal place of office at 2525 NW Expressway, Suite 105 Oklahoma City,  Oklahoma 73112, and Brokers National Life Assurance Company ("BNL"), with its principal place of office at 7010 Hwy. 71 W., Suite 100, Austin, Texas 78735.
- **parties:** This Outsourcing Agreement (" Agreement") is executed as of this 1 st  day of May 2006, by and between Virtual Item Processing Systems, Inc. ("VIP"), with its principal place of office at 2525 NW Expressway, Suite 105 Oklahoma City,  Oklahoma 73112, and Brokers National Life Assurance Company ("BNL"), with its principal place of office at 7010 Hwy. 71 W., Suite 100, Austin, Texas 78735.
- **agreement_date:** This Outsourcing Agreement (" Agreement") is executed as of this 1 st  day of May 2006
- **governing_law:** This Agreement and performance hereunder shall be governed by the laws of the State of Oklahoma without regard to conflict of laws.

<a id="case-28"></a>
### 28. GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement4.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:42:50 IST · **Model:** gemini-3.7-flash  
**Processing:** 19.044 seconds · **Recorded tokens:** 3770

[Source TXT](data/raw/contracts/batch_sample/GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content%20License%20Agreement4.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Fox Mobile Entertainment, Inc.<br>Glu Mobile Inc. | Fox Mobile Entertainment, Inc.<br>Glu Mobile Inc. | Match |
| Agreement date | 2007-02-19 | 2/19/07 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 5/5 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Fox Mobile Entertainment, Inc. ("Fox"); Glu Mobile Inc. ("Licensee")

**Supporting quotes:**

- **parties:** between Fox Mobile Entertainment, Inc. ("Fox"), as Administrator for Twentieth Century Fox Film Corporation, and Glu Mobile Inc. ("Licensee").
- **parties:** Fox Mobile Entertainment, Inc. ("Fox")
- **parties:** between Fox Mobile Entertainment, Inc. ("Fox"), as Administrator for Twentieth Century Fox Film Corporation, and Glu Mobile Inc. ("Licensee").
- **parties:** Glu Mobile Inc. ("Licensee")
- **agreement_date:** Dated as of February 19, 2007

<a id="case-29"></a>
### 29. GRIDIRONBIONUTRIENTS,INC_02_05_2020-EX-10.3-SUPPLY AGREEMENT.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:42:42 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.571 seconds · **Recorded tokens:** 2885

[Source TXT](data/raw/contracts/batch_sample/GRIDIRONBIONUTRIENTS%2CINC_02_05_2020-EX-10.3-SUPPLY%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | EWSD 1, LLC, d/b/a/ SHI FARMS<br>Gridiron BioNutrients, Inc | EWSD 1, LLC, d/b/a SHI FARMS<br>Gridiron BioNutrients | Mismatch |
| Agreement date | 2020-01-27 | 1/27/20 | Match |
| Governing law | State of Colorado | Colorado | Match |

**Date basis:** `signature_fallback`.

**Evidence presence:** 6/6 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** The two extracted legal entities include d/b/a Shi Farms. Reference omits Gridiron Inc. and has an additional collective-party phrase. Collective phrase is now separated, but the legal-name discrepancy stays flagged.

**Original CUAD parties answer:** EWSD 1, LLC, d/b/a SHI FARMS ("Shi Farms"); Gridiron BioNutrients ("Gridiron"); EWSD 1, LLC, d/b/a SHI FARMS and Gridiron BioNutrients (individually “a Party,” and collectively, “the Parties.”)

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** EWSD 1, LLC, d/b/a/ SHI FARMS ("Shi Farms"), a Delaware limited liability company
- **parties:** Gridiron BioNutrients, Inc, a Nevada Corporation ("Gridiron")
- **agreement_date:** IN WITNESS WHEREOF, the Parties have executed this Agreement as of the date below.
- **agreement_date:** Date: 1/26/2020
- **agreement_date:** Date: 1/27/2020
- **governing_law:** This Agreement and any amendments thereto shall be construed according to the laws of the State of Colorado without regard to conflicts of law principles and any disputes hereunder shall be litigated in a state court in Colorado.

<a id="case-30"></a>
### 30. NETGEAR,INC_04_21_2003-EX-10.16- AMENDMENT #2 TO THE DISTRIBUTION AGREEMENT.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:43:09 IST · **Model:** gemini-3.7-flash  
**Processing:** 9.945 seconds · **Recorded tokens:** 2759

[Source TXT](data/raw/contracts/batch_sample/NETGEAR%2CINC_04_21_2003-EX-10.16-%20AMENDMENT%20%232%20TO%20THE%20DISTRIBUTION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | INGRAM MICRO INC.<br>NETGEAR, INC. | Ingram Micro<br>NETGEAR, Inc. | Mismatch |
| Agreement date | 1998-07-15 | 7/15/98 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** Amendment #2 explicitly names INGRAM MICRO INC.; reference omits INC. Comparison intentionally remains false per user instruction. July 15, 1998 date still matches.

**Original CUAD parties answer:** Ingram Micro ("Distributor"); NETGEAR, Inc. ("NETGEAR")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** THIS AMENDMENT (the "Amendment") is entered into this 15th day of July 1998, by and between INGRAM MICRO INC. ("Ingram") and NETGEAR, INC. ("Vendor").
- **parties:** THIS AMENDMENT (the "Amendment") is entered into this 15th day of July 1998, by and between INGRAM MICRO INC. ("Ingram") and NETGEAR, INC. ("Vendor").
- **agreement_date:** THIS AMENDMENT (the "Amendment") is entered into this 15th day of July 1998

<a id="case-31"></a>
### 31. SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise Agreement3.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:43:19 IST · **Model:** gemini-3.7-flash  
**Processing:** 17.466 seconds · **Recorded tokens:** 3718

[Source TXT](data/raw/contracts/batch_sample/SoupmanInc_20150814_8-K_EX-10.1_9230148_EX-10.1_Franchise%20Agreement3.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | [] | [] | Match |
| Agreement date | null | null | Match |
| Governing law | New York | New York | Match |

**Evidence presence:** 1/1 quotes found (whitespace-normalized).

**Supporting quotes:**

- **governing_law:** The Master Franchise Agreement requires application of the laws of New York.

<a id="case-32"></a>
### 32. UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Affiliate Agreement.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:43:36 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.564 seconds · **Recorded tokens:** 4395

[Source TXT](data/raw/contracts/batch_sample/UnionDentalHoldingsInc_20050204_8-KA_EX-10_3345577_EX-10_Affiliate%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Dr. George D. Green<br>UNION DENTAL CORP. | Dr. George D. Green<br>UNION DENTAL CORP. | Match |
| Agreement date | 2005-01-28 | 1/28/05 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Dr. George D. Green ("Business Affiliate"); UNION DENTAL CORP. ("UDC")("parties" and singularly as a "Party")

**Supporting quotes:**

- **parties:** This  Business  Affiliate  Agreement   ("Agreement")  dated  January  28,  2005, effective  as of October 15,  2004,  ("Effective  Date") is entered  into by and between Dr. George D. Green (the "Business Affiliate") and UNION DENTAL CORP., a Florida  corporation  ("UDC")
- **parties:** This  Business  Affiliate  Agreement   ("Agreement")  dated  January  28,  2005, effective  as of October 15,  2004,  ("Effective  Date") is entered  into by and between Dr. George D. Green (the "Business Affiliate") and UNION DENTAL CORP., a Florida  corporation  ("UDC")
- **agreement_date:** This  Business  Affiliate  Agreement   ("Agreement")  dated  January  28,  2005

<a id="case-33"></a>
### 33. VEONEER,INC_02_21_2020-EX-10.11-JOINT VENTURE AGREEMENT.txt

**Cohort:** Revised prompt — regression  
**Saved extraction started:** 15 Oct 2026 11:43:42 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.736 seconds · **Recorded tokens:** 3644

[Source TXT](data/raw/contracts/batch_sample/VEONEER%2CINC_02_21_2020-EX-10.11-JOINT%20VENTURE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Veoneer AB<br>Veoneer US, Inc.<br>Nissin Kogyo Co., Ltd.<br>Nissin Kogyo Holdings USA, Inc.<br>Zhongshan Nissin Industry Co., Ltd. | Veoneer AB<br>Veoneer US, Inc.<br>Nissin Kogyo Co., Ltd.<br>Nissin Kogyo Holdings USA, Inc.<br>Zhongshan Nissin Industry Co., Ltd. | Match |
| Agreement date | 2019-10-30 | 10/30/19 | Match |
| Governing law | Japan | Japan | Match |

**Date basis:** `explicit`.

**Evidence presence:** 7/7 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Veoneer AB (“VeoneerAB”); Veoneer US, Inc. (“Veoneer US", and together with Veoneer AB, the “Veoneer Parties”); Nissin Kogyo Co., Ltd. (“Nissin”); Nissin Kogyo Holdings USA, Inc. (“NissinHolding”); Zhongshan Nissin Industry Co., Ltd. (“NBZ”, and together with Nissin andNissin Holding, the “Nissin Parties”)

**Supporting quotes:**

- **parties:** Veoneer AB, a Swedish corporation ("Veoneer AB")
- **parties:** Veoneer US, Inc., a Delaware corporation ("Veoneer US" and together with Veoneer AB, the "Veoneer Parties")
- **parties:** Nissin Kogyo Co., Ltd., a Japanese corporation ("Nissin")
- **parties:** Nissin Kogyo Holdings USA, Inc., an Ohio corporation ("Nissin Holding")
- **parties:** Zhongshan Nissin Industry Co., Ltd., a Peoples' Republic of China company ("NBZ" and together with Nissin and Nissin Holding, the "Nissin Parties")
- **agreement_date:** This AMENDMENT AND TERMINATION OF JOINT VENTURE AGREEMENT (this "Amendment") is made and entered into effective as of October 30, 2019
- **governing_law:** This Amendment shall be governed by and construed in accordance with the laws of Japan.

<a id="case-34"></a>
### 34. ALLISONTRANSMISSIONHOLDINGSINC_12_15_2014-EX-99.1-COOPERATION AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:43:50 IST · **Model:** gemini-3.7-flash  
**Processing:** 10.388 seconds · **Recorded tokens:** 9068

[Source TXT](data/raw/contracts/validation_round2/ALLISONTRANSMISSIONHOLDINGSINC_12_15_2014-EX-99.1-COOPERATION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Allison Transmission Holdings, Inc.<br>Gregory P. Spivy<br>VA Partners I, LLC<br>ValueAct Capital Master Fund, L.P.<br>ValueAct Capital Management, L.P.<br>ValueAct Capital Management, LLC<br>ValueAct Holdings, L.P.<br>ValueAct Holdings GP, LLC | VA Partners I, LLC, ValueAct Capital Master Fund, L.P., ValueAct Capital Management, L.P., ValueAct Capital Management, LLC, ValueAct Holdings, L.P. (collectively, the , and individually a  of the ValueAct Group)<br>Allison Transmission Holdings, Inc.<br>Gregory P. Spivy | Mismatch |
| Agreement date | 2014-12-12 | 12/12/14 | Match |
| Governing law | State of Delaware | Delaware | Match |

**Date basis:** `explicit`.

**Evidence presence:** 16/16 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** The opening incorporates Schedule A. Extraction includes the six named ValueAct entities listed there, the Company, and Gregory Spivy in his individual capacity. Reference groups several entities into one string and omits ValueAct Holdings GP, LLC. Keep the comparison flagged rather than splitting corporate names on commas.

**Original CUAD parties answer:** VA Partners I, LLC, ValueAct Capital Master Fund, L.P., ValueAct Capital Management, L.P., ValueAct Capital Management, LLC, ValueAct Holdings, L.P. (collectively, the “ValueAct Group”, and individually a “member” of the ValueAct Group); Allison Transmission Holdings, Inc. (the “Company”); Gregory P. Spivy (the “ValueAct Designee”)

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** Allison Transmission Holdings, Inc. (the "Company")
- **parties:** Gregory P. Spivy, in his individual capacity and as a member of the ValueAct Group (the "ValueAct Designee").
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** VA Partners I, LLC
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** ValueAct Capital Master Fund, L.P.
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** ValueAct Capital Management, L.P.
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** ValueAct Capital Management, LLC
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** ValueAct Holdings, L.P.
- **parties:** This Cooperation Agreement (this "Agreement") dated December 12, 2014, is by and among the persons and entities listed on Schedule A
- **parties:** ValueAct Holdings GP, LLC
- **agreement_date:** This Cooperation Agreement (this "Agreement") dated December 12, 2014
- **governing_law:** THIS AGREEMENT SHALL BE GOVERNED IN ALL RESPECTS, INCLUDING WITHOUT LIMITATION VALIDITY, INTERPRETATION AND EFFECT, BY THE LAWS OF THE STATE OF DELAWARE APPLICABLE TO CONTRACTS EXECUTED AND TO BE PERFORMED WHOLLY WITHIN SUCH STATE WITHOUT GIVING EFFECT TO THE CHOICE OF LAW PRINCIPLES OF SUCH STATE.

<a id="case-35"></a>
### 35. BLUEROCKRESIDENTIALGROWTHREIT,INC_06_01_2016-EX-1.1-AGENCY AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:00 IST · **Model:** gemini-3.7-flash  
**Processing:** 13.052 seconds · **Recorded tokens:** 28519

[Source TXT](data/raw/contracts/validation_round2/BLUEROCKRESIDENTIALGROWTHREIT%2CINC_06_01_2016-EX-1.1-AGENCY%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Bluerock Residential Growth REIT, Inc.<br>Bluerock Residential Holdings, L.P.<br>BRG Manager, LLC<br>Compass Point Research &amp; Trading, LLC | Bluerock Residential Growth REIT, Inc.<br>Bluerock Residential Holdings, L.P.  (collectively, Company, and Bluerock Residential Growth REIT, Inc. are referred to as the )<br>BRG Manager, LLC<br>Compass Point Research &amp; Trading, LLC | Mismatch |
| Agreement date | 2016-05-25 | 5/25/16 | Match |
| Governing law | State of New York | New York | Match |

**Date basis:** `defined_date`.

**Evidence presence:** 7/7 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** The four extracted entities match the opening. Reference attaches a collective Transaction Entities definition to the Operating Partnership. That non-alias parenthetical is deliberately left for review.

**Original CUAD parties answer:** Bluerock Residential Growth REIT, Inc. (“Company”); Bluerock Residential Holdings, L.P. (“Operating Partnership”) (collectively, Company, and Bluerock Residential Growth REIT, Inc. are referred to as the “Transaction Entities”); BRG Manager, LLC (“Manager”); Compass Point Research &amp; Trading, LLC (“Agent”)

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** Bluerock Residential Growth REIT, Inc., a Maryland corporation (the "Company")
- **parties:** Bluerock Residential Holdings, L.P., a Delaware limited partnership for which the Company is the sole general partner (the "Operating Partnership" and together with the Company, the "Transaction Entities")
- **parties:** BRG Manager, LLC, a Delaware limited liability company (the "Manager")
- **parties:** Compass Point Research &amp; Trading, LLC, acting as agent (the "Agent")
- **agreement_date:** The foregoing Agreement is hereby confirmed and accepted as of the date first above written.
- **agreement_date:** May 25, 2016
- **governing_law:** This Agreement shall be governed by, and construed in accordance with, the laws of the State of New York.

<a id="case-36"></a>
### 36. EMERALDHEALTHTHERAPEUTICSINC_06_10_2020-EX-4.5-CONSULTING AGREEMENT - DR. GAETANO MORELLO N.D. INC..txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:13 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.886 seconds · **Recorded tokens:** 5786

[Source TXT](data/raw/contracts/validation_round2/EMERALDHEALTHTHERAPEUTICSINC_06_10_2020-EX-4.5-CONSULTING%20AGREEMENT%20-%20DR.%20GAETANO%20MORELLO%20N.D.%20INC..txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | EMERALD HEALTH NATURALS, INC.<br>DR. GAETANO MORELLO N.D. INC. | EMERALD HEALTH NATURALS, INC<br>DR. GAETANO MORELLO N.D. INC | Match |
| Agreement date | 2019-01-10 | 1/10/19 | Match |
| Governing law | laws of British Columbia and the federal laws of Canada applicable in British Columbia | British Columbia, Canada | Mismatch |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — governing_law (Reviewed reference/scope difference):** Source expressly includes British Columbia law and applicable Canadian federal law. Extraction preserves both; reference compresses this to British Columbia, Canada. Federal-law detail remains visible rather than being dropped for matching.

**Original CUAD parties answer:** EMERALD HEALTH NATURALS, INC (“Emerald”, “Company”); DR. GAETANO MORELLO N.D. INC ("Contractor")

**Saved review reasons:**

- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** EMERALD HEALTH NATURALS, INC., a company having its registered and records office at 7860 Venture Street, Burnaby, BC V5A 1V3<br><br>("Emerald" or the "Company")
- **parties:** DR. GAETANO MORELLO N.D. INC., Businessperson, having an office at 2975 East 4th Avenue, Vancouver, B.C. V5M 1L1<br><br>(the "Contractor")
- **agreement_date:** THIS AGREEMENT made effective the 10 day of January 2019 (the "Effective Date"),
- **governing_law:** This Agreement will be governed by and construed inaccordance with the laws of British Columbia and the federal laws of Canada applicable in British Columbia, and the parties irrevocably submit to and accept generally and unconditionally the exclusive jurisdiction of the courts and appellate courts of British Columbia in that regard.

<a id="case-37"></a>
### 37. EuromediaHoldingsCorp_20070215_10SB12G_EX-10.B(01)_525118_EX-10.B(01)_Content License Agreement.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:22 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.432 seconds · **Recorded tokens:** 7825

[Source TXT](data/raw/contracts/validation_round2/EuromediaHoldingsCorp_20070215_10SB12G_EX-10.B%2801%29_525118_EX-10.B%2801%29_Content%20License%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Rogers Cable Communications Inc.<br>EuroMedia Holdings Corp. | Rogers Cable Communications Inc.<br>EuroMedia Holdings Corp. | Match |
| Agreement date | 2006-07-11 | 7/11/06 | Match |
| Governing law | Province of Ontario and the federal laws of Canada applicable therein | Ontario, Canada | Mismatch |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — governing_law (Reviewed reference/scope difference):** Source expressly includes Ontario and applicable Canadian federal law. Extraction preserves both; reference says Ontario, Canada. Leave the reference comparison flagged.

**Original CUAD parties answer:** Rogers Cable Communications Inc. ("Rogers"); EuroMedia Holdings Corp. ("Licensor")

**Saved review reasons:**

- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** VIDEO-ON-DEMAND CONTENT LICENSE AGREEMENT between Rogers Cable Communications Inc. ("Rogers") and EuroMedia Holdings Corp. ("Licensor")
- **parties:** VIDEO-ON-DEMAND CONTENT LICENSE AGREEMENT between Rogers Cable Communications Inc. ("Rogers") and EuroMedia Holdings Corp. ("Licensor")
- **agreement_date:** made as of July 11 , 2006
- **governing_law:** This Agreement shall be governed by laws of the Province of Ontario and the federal laws of Canada applicable therein.

<a id="case-38"></a>
### 38. INGEVITYCORP_05_16_2016-EX-10.5-INTELLECTUAL PROPERTY AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:30 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.933 seconds · **Recorded tokens:** 14634

[Source TXT](data/raw/contracts/validation_round2/INGEVITYCORP_05_16_2016-EX-10.5-INTELLECTUAL%20PROPERTY%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | WestRock Company<br>Ingevity Corporation | WestRock Company<br>Ingevity Corporation | Match |
| Agreement date | 2016-05-14 | 5/14/16 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Original CUAD parties answer:** WestRock Company ("Parent"); Ingevity Corporation ("SpinCo"); SpinCo and Parent (individually referred to herein as a “Party” and collectively as the “Parties”)

**Supporting quotes:**

- **parties:** WestRock Company, a Delaware corporation ("Parent")
- **parties:** Ingevity Corporation, a Delaware corporation ("SpinCo")
- **agreement_date:** This INTELLECTUAL PROPERTY AGREEMENT, dated as of May 14, 2016 (this "Agreement"), is by and between WestRock Company, a Delaware corporation ("Parent"), and Ingevity Corporation, a Delaware corporation ("SpinCo").

<a id="case-39"></a>
### 39. N2KINC_10_16_1997-EX-10.16-SPONSORSHIP AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:37 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.406 seconds · **Recorded tokens:** 9726

[Source TXT](data/raw/contracts/validation_round2/N2KINC_10_16_1997-EX-10.16-SPONSORSHIP%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Excite, Inc.<br>N2K Inc. | Excite, Inc.<br>N2K, Inc. | Match |
| Agreement date | 1997-09-23 | 9/23/97 | Match |
| Governing law | the State of New York | New York | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Excite, Inc. ("Excite"); N2K, Inc. ("Sponsor")

**Supporting quotes:**

- **parties:** Excite, Inc., a California corporation, located at 555 Broadway, Redwood City, California 94063 ("Excite")
- **parties:** N2K Inc., a Pennsylvania corporation, located at 55 Broad Street, 26th Floor, New York, New York, 10004 ("Sponsor")
- **agreement_date:** This agreement ("Agreement") is entered into as of the 23rd day of September, 1997 ("Effective Date")
- **governing_law:** This Agreement will be governed by and construed in accordance with the laws of the State of New York

<a id="case-40"></a>
### 40. PACIFICSYSTEMSCONTROLTECHNOLOGYINC_08_24_2000-EX-10.53-SPONSORSHIP AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:44 IST · **Model:** gemini-3.7-flash  
**Processing:** 13.225 seconds · **Recorded tokens:** 3339

[Source TXT](data/raw/contracts/validation_round2/PACIFICSYSTEMSCONTROLTECHNOLOGYINC_08_24_2000-EX-10.53-SPONSORSHIP%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | American Champion Media, Inc.<br>Shun Li De Commerce &amp; Trading Ltd | American Champion Media,<br>Shun Li De Commerce &amp; Trading Ltd, | Mismatch |
| Agreement date | 2000-04-14 | 4/14/00 | Match |
| Governing law | State of California and Hong Kong | California; Hong Kong | Mismatch |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** The source names American Champion Media, Inc.; reference drops Inc. Law clause explicitly names both California and Hong Kong; reference separates these with a semicolon. Both comparisons remain flagged without suffix removal or fuzzy jurisdiction matching.

**Review — governing_law (Reviewed reference/scope difference):** The source names American Champion Media, Inc.; reference drops Inc. Law clause explicitly names both California and Hong Kong; reference separates these with a semicolon. Both comparisons remain flagged without suffix removal or fuzzy jurisdiction matching.

**Original CUAD parties answer:** American Champion Media, ("ACM"); Shun Li De Commerce &amp; Trading Ltd, ("SLD")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.
- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** American Champion Media, Inc. ("ACM"), a Delaware company with headquarters at 1694 The Alameda, San Jose, CA 95126, U.S.A., is the  host and producer of a boxing event to take place at the Tian He Stadium in Guangzhou, China (the "Event").
- **parties:** Shun Li De Commerce &amp; Trading Ltd
- **agreement_date:** this Sponsorship Agreement (the  "Agreement") dated as of April 14, 2000 is made by and between Shun Li  De Commerce &amp; Trading Ltd ("SLD") a Beijing company, with headquarters at Xin Xing Dong Xiang, Bldg 1 Suite 1413, Xi Cheng District, Beijing, China (the "Sponsor") and ACM.
- **governing_law:** This Agreement shall be governed by, and construed and enforced in accordance with, the laws of the State of California and the laws of Hong Kong.

<a id="case-41"></a>
### 41. PrecheckHealthServicesInc_20200320_8-K_EX-99.2_12070169_EX-99.2_Distributor Agreement.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:44:57 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.359 seconds · **Recorded tokens:** 2400

[Source TXT](data/raw/contracts/validation_round2/PrecheckHealthServicesInc_20200320_8-K_EX-99.2_12070169_EX-99.2_Distributor%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Co-Diagnostics, Inc.<br>PreCheck Health Services, Inc. | Co-Diagnostics, Inc.<br>PreCheck Health Services, Inc. | Match |
| Agreement date | 2020-03-19 | 3/19/20 | Match |
| Governing law | State of Texas | Texas | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Co-Diagnostics, Inc. ("Principal"); PreCheck Health Services, Inc. ("Distributor")

**Supporting quotes:**

- **parties:** Between: Co-Diagnostics, Inc. (herein referred to as "Principal")
- **parties:** And PreCheck Health Services, Inc. (herein referred to as "Distributor").
- **agreement_date:** Agreement made this 19t h day of March, 2020
- **governing_law:** This Agreement shall be construed in accordance with and governed by the laws of the State of Texas without regard to principles of conflicts of laws.

<a id="case-42"></a>
### 42. RISEEDUCATIONCAYMANLTD_04_17_2020-EX-4.23-SERVICE AGREEMENT.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:45:02 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.639 seconds · **Recorded tokens:** 4650

[Source TXT](data/raw/contracts/validation_round2/RISEEDUCATIONCAYMANLTD_04_17_2020-EX-4.23-SERVICE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Rise (Tianjin) Education Information Consulting Co., Ltd. | Rise (Tianjin) Education Information Consulting Co., Ltd.<br>[*] | Mismatch |
| Agreement date | null | null | Match |
| Governing law | null | Beijing | Mismatch |

**Evidence presence:** 1/1 quotes found (whitespace-normalized).

**Review — parties (Reviewed reference/scope difference):** The other party is an unfilled placeholder, not an available legal name. Section 12 specifies Beijing Arbitration Commission arbitration, but does not state governing law; reference Beijing has no annotated governing-law evidence. Extraction null avoids confusing arbitral venue with governing law.

**Review — governing_law (Reviewed reference/scope difference):** The other party is an unfilled placeholder, not an available legal name. Section 12 specifies Beijing Arbitration Commission arbitration, but does not state governing law; reference Beijing has no annotated governing-law evidence. Extraction null avoids confusing arbitral venue with governing law.

**Original CUAD parties answer:** Rise (Tianjin) Education Information Consulting Co., Ltd. ("Service Provider"); [*] ("Service Recipient")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.
- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** Party A: Rise (Tianjin) Education Information Consulting Co., Ltd. ("Service Provider")

<a id="case-43"></a>
### 43. SENMIAOTECHNOLOGYLTD_02_19_2019-EX-10.5-Collaboration Agreement.txt

**Cohort:** Revised prompt — first unseen set  
**Saved extraction started:** 15 Oct 2026 11:45:10 IST · **Model:** gemini-3.7-flash  
**Processing:** 17.794 seconds · **Recorded tokens:** 19230

[Source TXT](data/raw/contracts/validation_round2/SENMIAOTECHNOLOGYLTD_02_19_2019-EX-10.5-Collaboration%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Didi Chuxing Technology Co., Ltd.<br>Hunan Ruixi Financial Leasing Co., Ltd | Didi Chuxing Technology Co., Ltd.<br>Hunan Ruixi Financial Leasing Co., Ltd | Match |
| Agreement date | 2018-12-17 | 12/17/18 | Match |
| Governing law | China | China | Match |

**Date basis:** `signature_fallback`.

**Evidence presence:** 5/5 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Didi Chuxing Technology Co., Ltd. ("Party A"); Hunan Ruixi Financial Leasing Co., Ltd ("Party B"); Party A and Party B (individually referred to as a “Party” and collectively as the “Parties”)

**Supporting quotes:**

- **parties:** Party A: Didi Chuxing Technology Co., Ltd.
- **parties:** Party B: Hunan Ruixi Financial Leasing Co., Ltd
- **agreement_date:** The Agreement executed offline in paper form shall become effective upon the completion of the execution by both Parties (hereinafter referred to as the "Effective Date"); and the Agreement executed online in electronic form shall become effective upon the completion of the execution on the Contracting Platform by both Parties (hereinafter referred to as the "Effective Date") recorded by the third-party Online Document Depository.
- **agreement_date:** [signature authenticated by third party document depository on December 17, 2018]
- **governing_law:** The execution, validation, interpretation, performance, modification and termination of this Agreement and the settlement of disputes under this Agreement shall be governed by the Laws of China.

<a id="case-44"></a>
### 44. ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorship Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:56:23 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.854 seconds · **Recorded tokens:** 5255

[Source TXT](data/raw/contracts/final_validation_sample/ArcGroupInc_20171211_8-K_EX-10.1_10976103_EX-10.1_Sponsorship%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Jacksonville Jaguars, LLC<br>The ARC Group, Inc. | Jacksonville Jaguars, LLC<br>The ARC Group, Inc. | Match |
| Agreement date | 2017-11-27 | 11/27/17 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Jacksonville Jaguars, LLC ("Club"); The ARC Group, Inc. ("Sponser")

**Supporting quotes:**

- **parties:** Jacksonville Jaguars, LLC, a Delaware limited liability company ("Club")
- **parties:** The ARC Group, Inc., a Florida corporation (owner and operator of Dick's Wings and Grill) ("Sponsor")
- **agreement_date:** This Sponsorship Agreement (this "Agreement") is entered into as of November 27, 2017

<a id="case-45"></a>
### 45. BellringBrandsInc_20190920_S-1_EX-10.12_11817081_EX-10.12_Manufacturing Agreement2.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:56:31 IST · **Model:** gemini-3.7-flash  
**Processing:** 7.122 seconds · **Recorded tokens:** 2182

[Source TXT](data/raw/contracts/final_validation_sample/BellringBrandsInc_20190920_S-1_EX-10.12_11817081_EX-10.12_Manufacturing%20Agreement2.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Stremick's Heritage Foods, LLC<br>Premier Nutrition Corporation | Stremick's Heritage Foods, LLC<br>Premier Nutrition Corporation | Match |
| Agreement date | 2018-06-11 | 6/11/18 | Match |
| Governing law | null | null | Match |

**Date basis:** `defined_date`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Stremick's Heritage Foods, LLC ("Heritage"); Premier Nutrition Corporation ("Premier")

**Supporting quotes:**

- **parties:** This Amendment No. 1 (the "Amendment"), entered into by and between Stremick's Heritage Foods, LLC ("Heritage") Premier Nutrition Corporation ("Premier")
- **parties:** This Amendment No. 1 (the "Amendment"), entered into by and between Stremick's Heritage Foods, LLC ("Heritage") Premier Nutrition Corporation ("Premier")
- **agreement_date:** IN WITNESS WHEREOF, the Parties have caused this Amendment to be signed by their respective duly authorized representatives as of the Amendment Effective Date.
- **agreement_date:** is effective as of June 11, 2018 ("Amendment Effective Date")

<a id="case-46"></a>
### 46. CHINARECYCLINGENERGYCORP_11_14_2013-EX-10.6-Cooperation Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:56:39 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.843 seconds · **Recorded tokens:** 4674

[Source TXT](data/raw/contracts/final_validation_sample/CHINARECYCLINGENERGYCORP_11_14_2013-EX-10.6-Cooperation%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Xi'an Zhonghong New Energy Technology Co., Ltd.<br>Boxing County Chengli Gas Supply Co., Ltd. | Xi'an Zhonghong New Energy Technology Co., Ltd.<br>Boxing County Chengli Gas Supply Co., Ltd. | Match |
| Agreement date | null | 07/[]/2013 | Unscored — review |
| Governing law | null | null | Match |

**Evidence presence:** 2/2 quotes found (whitespace-normalized).

**Review — agreement_date (incomplete reference):** Source and reference give July 2013 without a day. Null is appropriate for the complete-date schema; the comparison remains unscored.

**Original CUAD parties answer:** Xi'an Zhonghong New Energy Technology Co., Ltd. ("Party A"); Boxing County Chengli Gas Supply Co., Ltd. ("Party B")

**Saved review reasons:**

- agreement_date: Incomplete or conflicting reference dates; manual review required.

**Supporting quotes:**

- **parties:** Party A: Xi'an Zhonghong New Energy Technology Co., Ltd.
- **parties:** Party B: Boxing County Chengli Gas Supply Co., Ltd.

<a id="case-47"></a>
### 47. FuelcellEnergyInc_20191106_8-K_EX-10.1_11868007_EX-10.1_Development Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:56:45 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.594 seconds · **Recorded tokens:** 23788

[Source TXT](data/raw/contracts/final_validation_sample/FuelcellEnergyInc_20191106_8-K_EX-10.1_11868007_EX-10.1_Development%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | ExxonMobil Research and Engineering Company<br>FuelCell Energy, Inc. | ExxonMobil Research and Engineering Company<br>FuelCell Energy, Inc. | Match |
| Agreement date | 2019-10-31 | 11/5/19 | Mismatch |
| Governing law | State of New York | New York | Match |

**Date basis:** `defined_date`.

**Evidence presence:** 5/5 quotes found (whitespace-normalized).

**Review — agreement_date (date convention disagreement):** Opening says made as of the Effective Date; Appendix A defines October 31, 2019. Both signatures are November 5, 2019, which CUAD uses. Extraction follows our documented as-of/defined-date precedence, but differs from CUAD's execution-date convention here. Both dates exist; do not call this a spelling error or force a match.

**Original CUAD parties answer:** ExxonMobil Research and Engineering Company (“ExxonMobil”); FuelCell Energy, Inc. (“FCE”)

**Saved review reasons:**

- agreement_date: Agreement dates differ; review date selection and evidence.

**Supporting quotes:**

- **parties:** ExxonMobil Research and Engineering Company, a corporation of the State of Delaware having offices at 1545 Route 22 East, Annandale, New Jersey 08801 ("ExxonMobil"); and
- **parties:** FuelCell Energy, Inc., a corporation of the State of Delaware having offices at 3 Great Pasture Road, Danbury, Connecticut 06810 ("FCE").
- **agreement_date:** This Agreement is made as of the Effective Date between:
- **agreement_date:** "Effective Date" means October 31, 2019.
- **governing_law:** The validity and interpretation of this Agreement and the legal relations of the Parties to it will be governed by the laws of the State of New York without recourse to its conflicts of law rules.

<a id="case-48"></a>
### 48. GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content License Agreement2.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:57:01 IST · **Model:** gemini-3.7-flash  
**Processing:** 22.338 seconds · **Recorded tokens:** 6924

[Source TXT](data/raw/contracts/final_validation_sample/GluMobileInc_20070319_S-1A_EX-10.09_436630_EX-10.09_Content%20License%20Agreement2.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Glu Mobile, Inc. f/k/a Sorrent, Inc.<br>Fox Mobile Entertainment, Inc. | Fox Mobile Entertainment<br>Glu Mobile, Inc. f/k/a Sorrent, Inc. | Mismatch |
| Agreement date | 2005-11-11 | 11/18/05 | Mismatch |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Review — parties (reference/evaluator):** Amendment substitutes Fox Mobile Entertainment, Inc. for the earlier Fox division, and acknowledges Glu's change of name. Extracted entities are supported; reference omits Fox's Inc. suffix.

**Review — agreement_date (date convention disagreement):** Amendment is explicitly dated November 11, 2005; signatures are November 18, 2005. Extraction follows the explicit-date rule. CUAD's answer uses November 18 but its evidence column lists November 11, so reference answer/evidence and date convention differ. Both remain visible.

**Original CUAD parties answer:** Fox Mobile Entertainment ("Fox"); Glu Mobile, Inc. f/k/a Sorrent, Inc. ("Licensee")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.
- agreement_date: Agreement dates differ; review date selection and evidence.

**Supporting quotes:**

- **parties:** Glu Mobile, Inc. f/k/a Sorrent, Inc. ("Licensee")
- **parties:** Fox Mobile Entertainment, Inc. ("Fox")
- **agreement_date:** Dated as of November 11, 2005

<a id="case-49"></a>
### 49. GSVINC_05_15_1998-EX-10-SPONSORSHIP AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:56:54 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.478 seconds · **Recorded tokens:** 10243

[Source TXT](data/raw/contracts/final_validation_sample/GSVINC_05_15_1998-EX-10-SPONSORSHIP%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Excite, Inc.<br>CyberShop | Excite, Inc.<br>CyberShop | Match |
| Agreement date | 1998-03-31 | 3/31/98 | Match |
| Governing law | State of New York | New York | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Excite, Inc."Excite"; CyberShop "Client"

**Supporting quotes:**

- **parties:** Excite, Inc., a California corporation, located at 555 Broadway, Redwood City, California 94063
- **parties:** CyberShop, a Delaware corporation, located at 130 Madison Avenue, New York, New York 10016
- **agreement_date:** This agreement ("Agreement") is entered into as of the 31st day of March, 1998
- **governing_law:** This Agreement will be governed by and construed in accordance with the laws of the State of New York, notwithstanding the actual state or country of residence or incorporation of Excite or Client.

<a id="case-50"></a>
### 50. INNOVIVA,INC_08_07_2014-EX-10.1-COLLABORATION AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:57:23 IST · **Model:** gemini-3.7-flash  
**Processing:** 8.761 seconds · **Recorded tokens:** 41312

[Source TXT](data/raw/contracts/final_validation_sample/INNOVIVA%2CINC_08_07_2014-EX-10.1-COLLABORATION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | THERAVANCE, INC.<br>GLAXO GROUP LIMITED | Theravance, Inc.<br>Glaxo Group Limited | Match |
| Agreement date | 2002-11-14 | 11/14/02 | Match |
| Governing law | State of Delaware | Delaware | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Theravance, Inc. ("Theravance"); Glaxo Group Limited ("GSK"); (Theravance and GSK, a “Party” or together, the “Parties”)

**Supporting quotes:**

- **parties:** This COLLABORATION AGREEMENT ("Agreement") dated November 14, 2002, is made by and between THERAVANCE, INC., a Delaware corporation, and having its principal office at 901 Gateway Boulevard, South San Francisco, California 94080 ("Theravance"), and GLAXO GROUP LIMITED, a United Kingdom corporation, and having its principal office at Glaxo Wellcome House, Berkeley Avenue, Greenford, Middlesex, UB6 0NN, United Kingdom ("GSK").
- **parties:** This COLLABORATION AGREEMENT ("Agreement") dated November 14, 2002, is made by and between THERAVANCE, INC., a Delaware corporation, and having its principal office at 901 Gateway Boulevard, South San Francisco, California 94080 ("Theravance"), and GLAXO GROUP LIMITED, a United Kingdom corporation, and having its principal office at Glaxo Wellcome House, Berkeley Avenue, Greenford, Middlesex, UB6 0NN, United Kingdom ("GSK").
- **agreement_date:** This COLLABORATION AGREEMENT ("Agreement") dated November 14, 2002, is made by and between THERAVANCE, INC., a Delaware corporation, and having its principal office at 901 Gateway Boulevard, South San Francisco, California 94080 ("Theravance"), and GLAXO GROUP LIMITED, a United Kingdom corporation, and having its principal office at Glaxo Wellcome House, Berkeley Avenue, Greenford, Middlesex, UB6 0NN, United Kingdom ("GSK").
- **governing_law:** This Agreement shall be construed, and the respective rights of the Parties determined, according to the substantive law of the State of Delaware notwithstanding the provisions governing conflict of laws under such Delaware law to the contrary, except matters of intellectual property law which shall be determined in accordance with the intellectual property laws relevant to the intellectual property in question.

<a id="case-51"></a>
### 51. KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:57:32 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.878 seconds · **Recorded tokens:** 37678

[Source TXT](data/raw/contracts/final_validation_sample/KINGPHARMACEUTICALSINC_08_09_2006-EX-10.1-PROMOTION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Depomed, Inc.<br>King Pharmaceuticals, Inc. | Depomed, Inc.<br>King Pharmaceuticals, Inc. | Match |
| Agreement date | 2006-06-27 | 6/27/06 | Match |
| Governing law | the State of New York | New York | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Depomed, Inc. ("Depomed"); King Pharmaceuticals, Inc. ("King"); Depomed and King (individually as a "party" and collectively as the "parties")

**Supporting quotes:**

- **parties:** Depomed, Inc., a California corporation ("Depomed")
- **parties:** King Pharmaceuticals, Inc., a Tennessee corporation ("King")
- **agreement_date:** This PROMOTION AGREEMENT (this "Agreement") is made as of June 27, 2006 (the "Effective Date"), by and between Depomed, Inc., a California corporation ("Depomed"), and King Pharmaceuticals, Inc., a Tennessee corporation ("King").
- **governing_law:** This Agreement will be construed under and in accordance with, and governed in all respects by, the laws of the State of New York, without regard to its conflicts of law principles.

<a id="case-52"></a>
### 52. LegacyEducationAllianceInc_20141110_8-K_EX-10.9_8828866_EX-10.9_Endorsement Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:57:45 IST · **Model:** gemini-3.7-flash  
**Processing:** 20.383 seconds · **Recorded tokens:** 7917

[Source TXT](data/raw/contracts/final_validation_sample/LegacyEducationAllianceInc_20141110_8-K_EX-10.9_8828866_EX-10.9_Endorsement%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Tigrent Learning UK Limited<br>Celebrity Speakers<br>Robbie Fowler | Tigrent Learning UK Limited<br>Celebrity Speakers<br>Robbie Fowler | Match |
| Agreement date | null | []/[]/2013 | Unscored — review |
| Governing law | England and Wales | England, United Kingdom; Wales, United Kingdom | Mismatch |

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — agreement_date (incomplete reference):** Source leaves day and month blank and states only 2013. Extraction null avoids inventing a full date; comparison remains unscored.

**Review — governing_law (reference/evaluator):** Source explicitly says England and Wales, as extracted. Reference expands it into two United Kingdom-qualified entries. Same named jurisdiction wording is represented differently, so the conservative comparator flags it.

**Original CUAD parties answer:** Tigrent Learning UK Limited ("Company"); Celebrity Speakers ("CSA"); Robbie Fowler ("Talent")

**Saved review reasons:**

- agreement_date: Incomplete or conflicting reference dates; manual review required.
- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** Tigrent Learning UK Limited of Boston House, 69 — 75 Boston Manor Road, Brentford, Middlesex, TW8 9.1J ("Company")
- **parties:** Celebrity Speakers of 90 High Street, Burnham, Buckinghamshire, SL1 7JT ("CSA") agent for Robbie Fowler ("Talent") in his individual capacity or his duly appointed Representative
- **parties:** Celebrity Speakers of 90 High Street, Burnham, Buckinghamshire, SL1 7JT ("CSA") agent for Robbie Fowler ("Talent") in his individual capacity or his duly appointed Representative
- **governing_law:** This Agreement shall be governed by the laws of England and Wales, and all actions brought hereunder whether at law or in equity shall be brought in England.

<a id="case-53"></a>
### 53. LIGHTBRIDGECORP_11_23_2015-EX-10.26-STRATEGIC ALLIANCE AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:57:39 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.494 seconds · **Recorded tokens:** 5337

[Source TXT](data/raw/contracts/final_validation_sample/LIGHTBRIDGECORP_11_23_2015-EX-10.26-STRATEGIC%20ALLIANCE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Lightbridge Corporation<br>Lloyds Register FNMA | Lightbridge Corporation<br>Lloyds Register FNMA<br>and together with | Mismatch |
| Agreement date | 2012-08-16 | 8/16/12 | Match |
| Governing law | England | England | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — parties (reference/evaluator):** Both named entities match the opening. CUAD adds a quoted alias-list phrase as a third entry; after alias cleaning it becomes and together with. No third legal entity is missing from the extraction.

**Original CUAD parties answer:** Lightbridge Corporation ("Lightbridge"); Lloyds Register FNMA ("Lloyds"); "Lloyds" and together with "Lightbridge" ("Parties")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** Lightbridge Corporation, a Nevada Corporation  ("Lightbridge")
- **parties:** Lloyds Register FNMA, acting through its office in Abu Dhabi ("Lloyds" and. together with Lightbridge. the "Parties")
- **agreement_date:** This STRATEGIC' ALLIANCE AGREEMENT (including the exhibits and schedules hereto, this "Agreement") is made and entered into this 16 day of August. 2012
- **governing_law:** The terms of this Agreement shall be governed by and construed in accordance with the laws of England.

<a id="case-54"></a>
### 54. NEONSYSTEMSINC_03_01_1999-EX-10.5-DISTRIBUTOR AGREEMENT_Amendment.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:58:05 IST · **Model:** gemini-3.7-flash  
**Processing:** 33.729 seconds · **Recorded tokens:** 10652

[Source TXT](data/raw/contracts/final_validation_sample/NEONSYSTEMSINC_03_01_1999-EX-10.5-DISTRIBUTOR%20AGREEMENT_Amendment.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Peregrine/Bridge Transfer Corporation<br>NEON Systems, Inc. | Peregrine/Bridge Transfer Corporation<br>Neon Systems, Inc. | Match |
| Agreement date | 1999-01-01 | 1/1/99 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Peregrine/Bridge Transfer Corporation ("Licensor"); Neon Systems, Inc. ("Licensee")

**Supporting quotes:**

- **parties:** THIS FIRST AMENDMENT TO DISTRIBUTOR AGREEMENT (this "Amendment") is made and entered into as of the 1st day of January, 1999, by and between Peregrine/Bridge Transfer Corporation, a Delaware corporation ("Licensor"), and NEON Systems, Inc., a Delaware corporation ("Licensee").
- **parties:** THIS FIRST AMENDMENT TO DISTRIBUTOR AGREEMENT (this "Amendment") is made and entered into as of the 1st day of January, 1999, by and between Peregrine/Bridge Transfer Corporation, a Delaware corporation ("Licensor"), and NEON Systems, Inc., a Delaware corporation ("Licensee").
- **agreement_date:** THIS FIRST AMENDMENT TO DISTRIBUTOR AGREEMENT (this "Amendment") is made and entered into as of the 1st day of January, 1999, by and between Peregrine/Bridge Transfer Corporation, a Delaware corporation ("Licensor"), and NEON Systems, Inc., a Delaware corporation ("Licensee").

<a id="case-55"></a>
### 55. OPERALTD_04_30_2020-EX-4.14-SERVICE AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:58:39 IST · **Model:** gemini-3.7-flash  
**Processing:** 6.542 seconds · **Recorded tokens:** 5645

[Source TXT](data/raw/contracts/final_validation_sample/OPERALTD_04_30_2020-EX-4.14-SERVICE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | PC Financial Services Private Limited<br>Mobimagic Co., Ltd. | PC Financial Services Private Limited<br>Mobimagic Co., Ltd. | Match |
| Agreement date | 2019-04-01 | 4/1/19 | Match |
| Governing law | India | India | Match |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Original CUAD parties answer:** PC Financial Services Private Limited ("PC Financial"); Mobimagic Co., Ltd. ("Mobimagic"); (each as "Party" collectively as "Parties")

**Supporting quotes:**

- **parties:** PC Financial Services Private Limited, a India company with an address at Building RZ-2, Pole No.-3, G/F Kapashera, Near HDFC Bank, New Delhi ("PC Financial"), a registered Non-banking Financial Company (NBFC) in India;
- **parties:** Mobimagic Co., Ltd., a company Incorporated under the laws of the People 's Republic of China with its principal place of business at Room 1110-046, A District, No. 1 Building, No.18 East Road, Zhongguancun, Haidlan District, Beijing City ("Mobimagic").
- **agreement_date:** This Service Agreement ("Agreement") is entered into on April. 1st 2019
- **governing_law:** This Agreement (and any question about its subsistence, effect or termination) is to be interpreted in accordance with the laws of India, save for that body of law which governs the conflict of laws.

<a id="case-56"></a>
### 56. QBIOMEDINC_04_08_2020-EX-99.1-JOINT FILING AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:58:46 IST · **Model:** gemini-3.7-flash  
**Processing:** 14.943 seconds · **Recorded tokens:** 3903

[Source TXT](data/raw/contracts/final_validation_sample/QBIOMEDINC_04_08_2020-EX-99.1-JOINT%20FILING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | YA II PN, Ltd.<br>YA Global Investments II (U.S.), Ltd.<br>Yorkville Advisors Global, LP<br>Yorkville Advisors Global II, LLC<br>YAII GP, LP<br>Yorkville Advisors GP, LLC<br>D-Beta One EQ, Ltd.<br>D-Beta One Blocker EQ, Ltd.<br>D-Beta One Growth and Opportunity Fund Offshore, LP<br>D-Beta One GP, LLC<br>Delta Beta Advisors, LP<br>Matthew Beckman | YA II PN, Ltd.<br>YA Global Investments II (U.S.), Ltd.<br>Yorkville Advisors Global, LP<br>Yorkville Advisors Global II, LLC<br>YAII GP, LP<br>Yorkville Advisors GP, LLC<br>D-Beta One EQ, Ltd.<br>D-Beta One Blocker EQ, Ltd.<br>D-Beta One Growth and Opportunity Fund Offshore, LP<br>D-Beta One GP, LLC<br>Delta Beta Advisors, LP | Mismatch |
| Agreement date | 2020-04-08 | 4/8/20 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 13/13 quotes found (whitespace-normalized).

**Review — parties (reference/scope review):** Matthew Beckman appears as a standalone /s/ undersigned with his own date at the end, without a corporate By or officer capacity. Model includes him while excluding the named corporate officer signing on behalf of entities. CUAD omits Matthew. This is an individual-party reference/scope difference, not clear evidence that the model confused an officer with a party.

**Original CUAD parties answer:** YA II PN, Ltd.; YA Global Investments II (U.S.), Ltd.; Yorkville Advisors Global, LP; Yorkville Advisors Global II, LLC; YAII GP, LP; Yorkville Advisors GP, LLC; D-Beta One EQ, Ltd.; D-Beta One Blocker EQ, Ltd.;<br>D-Beta One Growth and Opportunity Fund Offshore, LP; D-Beta One GP, LLC; Delta Beta Advisors, LP

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** YA II PN, Ltd.
- **parties:** YA Global Investments II (U.S.), Ltd.
- **parties:** Yorkville Advisors Global, LP
- **parties:** Yorkville Advisors Global II, LLC
- **parties:** YAII GP, LP
- **parties:** Yorkville Advisors GP, LLC
- **parties:** D-Beta One EQ, Ltd.
- **parties:** D-Beta One Blocker EQ, Ltd.
- **parties:** D-Beta One Growth and Opportunity Fund Offshore, LP
- **parties:** D-Beta One GP, LLC
- **parties:** Delta Beta Advisors, LP
- **parties:** Matthew Beckman
- **agreement_date:** Dated: 4/8/2020

<a id="case-57"></a>
### 57. ScansourceInc_20190822_10-K_EX-10.39_11793959_EX-10.39_Distributor Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:59:32 IST · **Model:** gemini-3.7-flash  
**Processing:** 22.444 seconds · **Recorded tokens:** 6618

[Source TXT](data/raw/contracts/final_validation_sample/ScansourceInc_20190822_10-K_EX-10.39_11793959_EX-10.39_Distributor%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Cisco Systems, Inc.<br>ScanSource, Inc. | Cisco Systems, Inc.<br>ScanSource, Inc. | Match |
| Agreement date | 2010-08-04 | 8/4/10 | Match |
| Governing law | null | null | Match |

**Date basis:** `signature_fallback`.

**Evidence presence:** 6/6 quotes found (whitespace-normalized).

**Original CUAD parties answer:** Cisco Systems, Inc. ("Cisco"); ScanSource, Inc. ("Distributor")

**Supporting quotes:**

- **parties:** Cisco Systems, Inc. ("Cisco"), a California corporation having Its principal place of business at 170 West Tasman Drive, San Jose, CA, 95134
- **parties:** ScanSource, Inc. ("Distributor"), a South Carolina corporation with a place of business at 6 Logue Court, Greenville, South Carolina, 29615
- **agreement_date:** IN WITNESS WHEREOF, the parties hereto have caused this Amendment No. 3 to be duly executed as of the Effective Date.
- **agreement_date:** is effective as of the date last signed below ("Amendment Effective Date").
- **agreement_date:** DATE: 8/4/10
- **agreement_date:** DATE: 7-29-10

<a id="case-58"></a>
### 58. SLINGERBAGINC_05_27_2020-EX-10.7-CONSULTING AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:59:01 IST · **Model:** gemini-3.7-flash  
**Processing:** 13.183 seconds · **Recorded tokens:** 9370

[Source TXT](data/raw/contracts/final_validation_sample/SLINGERBAGINC_05_27_2020-EX-10.7-CONSULTING%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Slinger Bag Inc.<br>Aitan Zacharin | Slinger Bag Inc.<br>Aitan Zacharin | Match |
| Agreement date | null | 04/30/[] | Unscored — review |
| Governing law | State of New York | New York | Match |

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Review — agreement_date (incomplete reference):** Opening gives 30th day of April without a year. Complete-date extraction stays null rather than borrowing a year from filing metadata. Reference 04/30/[] remains unscored.

**Original CUAD parties answer:** Slinger Bag Inc. (the "Company"); Aitan Zacharin ( the "Consultant")

**Saved review reasons:**

- agreement_date: Incomplete or conflicting reference dates; manual review required.

**Supporting quotes:**

- **parties:** Slinger Bag Inc., a Nevada company (the "Company")
- **parties:** Aitan Zacharin, an individual residing in Bet Shemesh, Israel (the "Consultant")
- **governing_law:** This Agreement will be construed and interpreted in accordance with the laws of the State of New York without reference to its conflicts of laws principles or the conflicts of laws principles of any other jurisdiction, and each of the parties hereto expressly attorns to the jurisdiction of the courts of the State of New York.

<a id="case-59"></a>
### 59. SMITHELECTRICVEHICLESCORP_04_04_2012-EX-10.26-FLEET MAINTENANCE AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:59:14 IST · **Model:** gemini-3.7-flash  
**Processing:** 9.034 seconds · **Recorded tokens:** 20149

[Source TXT](data/raw/contracts/final_validation_sample/SMITHELECTRICVEHICLESCORP_04_04_2012-EX-10.26-FLEET%20MAINTENANCE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | DAIRY CREST LIMITED<br>SEV GROUP LIMITED | DAIRY CREST LIMITED<br>SEV GROUP LIMITED | Match |
| Agreement date | 2005-10-13 | 10/13/05 | Match |
| Governing law | England and Wales | England; Wales | Mismatch |

**Date basis:** `explicit`.

**Evidence presence:** 4/4 quotes found (whitespace-normalized).

**Review — governing_law (reference/evaluator):** Source says law of England and Wales, as extracted. Reference separates England; Wales. Conservative string comparison flags equivalent jurisdiction wording.

**Original CUAD parties answer:** DAIRY CREST LIMITED ("DCL"); SEV GROUP LIMITED ("SEV")

**Saved review reasons:**

- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** DAIRY CREST LIMITED (Company no 2085882) whose registered office is at Claygate House, Littleworth Road,  Esher, Surrey KT10 9PN
- **parties:** SEV GROUP LIMITED (company no 4463640) whose registered office is at Unit 95/2, Tanfield Lea Industrial  Estate North, Stanley, Co Durham, DH9 9NX
- **agreement_date:** DATED         13 October 2005
- **governing_law:** This Agreement shall be governed by and construed in all respects in accordance with the law of England and Wales and both parties submit to the exclusive jurisdiction of the English Courts.

<a id="case-60"></a>
### 60. SPARKLINGSPRINGWATERHOLDINGSLTD_07_03_2002-EX-10.13-SOFTWARE LICENSE AND MAINTENANCE AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:59:23 IST · **Model:** gemini-3.7-flash  
**Processing:** 9.566 seconds · **Recorded tokens:** 6923

[Source TXT](data/raw/contracts/final_validation_sample/SPARKLINGSPRINGWATERHOLDINGSLTD_07_03_2002-EX-10.13-SOFTWARE%20LICENSE%20AND%20MAINTENANCE%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | GARMAN ROUTING SYSTEMS, INC.<br>SPARKLING SPRING WATER GROUP LIMITED | GARMAN ROUTING SYSTEMS, INC.<br>SPARKLING SPRING WATER GROUP LIMITED | Match |
| Agreement date | null | 05/[]/2000 | Unscored — review |
| Governing law | Nova Scotia and the laws of Canada applicable in Nova Scotia | Nova Scotia, Canada | Mismatch |

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Review — agreement_date (incomplete reference):** Source date is blank day of May 2000. Null is appropriate for the complete-date schema and remains unscored.

**Review — governing_law (reference/evaluator):** Source includes Nova Scotia law and applicable Canadian law. Extraction retains both; reference shortens it to Nova Scotia, Canada. Country/federal-law wording is not discarded to force a match.

**Original CUAD parties answer:** GARMAN ROUTING SYSTEMS, INC. ("GARMAN"); SPARKLING SPRING WATER GROUP LIMITED ("SPARKLING")

**Saved review reasons:**

- agreement_date: Incomplete or conflicting reference dates; manual review required.
- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** GARMAN ROUTING SYSTEMS, INC. ("GARMAN")
- **parties:** SPARKLING SPRING WATER GROUP LIMITED ("SPARKLING")
- **governing_law:** This Agreement shall be governed by the laws of Nova Scotia and the laws of Canada applicable in Nova Scotia.

<a id="case-61"></a>
### 61. VgrabCommunicationsInc_20200129_10-K_EX-10.33_11958828_EX-10.33_Development Agreement.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 12:00:01 IST · **Model:** gemini-3.7-flash  
**Processing:** 15.188 seconds · **Recorded tokens:** 6251

[Source TXT](data/raw/contracts/final_validation_sample/VgrabCommunicationsInc_20200129_10-K_EX-10.33_11958828_EX-10.33_Development%20Agreement.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | VGrab Asia Ltd.<br>Mr. Zheng Qing<br>Mr. Gu Xianwin<br>Ms. Chen Weijie | VGrab Asia Ltd.<br>Mr. Zheng Qing, Mr. Gu Xianwin and Ms. Chen Weijie | Mismatch |
| Agreement date | 2019-03-05 | 3/5/19 | Match |
| Governing law | Hong Kong | Hong Kong | Match |

**Date basis:** `explicit`.

**Evidence presence:** 6/6 quotes found (whitespace-normalized).

**Review — parties (reference/evaluator):** Source names VGrab Asia and three individual developers. Extraction lists all four separately; reference groups the three developers into one string. Same named participants, incompatible list granularity. Do not split arbitrary corporate names on commas to force matching.

**Original CUAD parties answer:** VGrab Asia Ltd. ("VAL"); Mr. Zheng Qing, Mr. Gu Xianwin and Ms. Chen Weijie ("Developer")

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** BETWEEN: VGrab Asia Ltd. (hereinafter called as the "VAL"), located at Room E, 6th Floor, Eastern Commercial Center, 397 Hennessy Road, Hong Kong.
- **parties:** AND: Mr. Zheng Qing, Mr. Gu Xianwin and Ms. Chen Weijie (hereinafter called as the "Developer"), a group of private software developers individuals' lead and coordinated by Ms. Chen Weijie with its operations in P.R.China.
- **parties:** AND: Mr. Zheng Qing, Mr. Gu Xianwin and Ms. Chen Weijie (hereinafter called as the "Developer"), a group of private software developers individuals' lead and coordinated by Ms. Chen Weijie with its operations in P.R.China.
- **parties:** AND: Mr. Zheng Qing, Mr. Gu Xianwin and Ms. Chen Weijie (hereinafter called as the "Developer"), a group of private software developers individuals' lead and coordinated by Ms. Chen Weijie with its operations in P.R.China.
- **agreement_date:** This Mobile Application Development Agreement (the "Agreement") is made and effective from 5th Day of March, 2019
- **governing_law:** This agreement shall be construed, interpreted and governed by and in accordance with the laws of Hong Kong.

<a id="case-62"></a>
### 62. VIVINT SOLAR, INC. - NON-COMPETITION AGREEMENT.txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 11:59:55 IST · **Model:** gemini-3.7-flash  
**Processing:** 5.738 seconds · **Recorded tokens:** 1934

[Source TXT](data/raw/contracts/final_validation_sample/VIVINT%20SOLAR%2C%20INC.%20-%20NON-COMPETITION%20AGREEMENT.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | VIVINT SOLAR, INC.<br>VIVINT, INC. | VIVINT SOLAR, INC. (together with its successors and permitted assigns, ) | Mismatch |
| Agreement date | 2017-08-16 | 8/16/17 | Match |
| Governing law | null | null | Match |

**Date basis:** `explicit`.

**Evidence presence:** 3/3 quotes found (whitespace-normalized).

**Review — parties (evaluator limitation):** The model correctly extracts Vivint Solar and Vivint as named in Amendment No. 1. Reference combines a real name, successor/assign scope and a collective-party sentence in one entry. Current collective-description cleanup drops that entire entry, so the evaluated reference loses Vivint, Inc. This is a remaining comparator defect/limitation, not a missing extracted company. Original reference is retained; no rules were changed during this final run.

**Original CUAD parties answer:** VIVINT SOLAR, INC. (together with its successors and permitted assigns, “VivintSolar”); VIVINT, INC. (together with its successors and permitted assigns “Vivint”) Vivint Solar and Vivint (individually as a “Party”, and collectively as the “Parties”)

**Saved review reasons:**

- parties: Party names or scope differ; review source and reference. No fuzzy matching or legal-suffix removal applied.

**Supporting quotes:**

- **parties:** VIVINT SOLAR, INC., a Delaware corporation
- **parties:** VIVINT, INC., a Utah corporation
- **agreement_date:** This NON-COMPETITION AGREEMENT AMENDMENT NO. 1 (this "Amendment") is entered into as of August 16, 2017

<a id="case-63"></a>
### 63. XENCORINC_10_25_2013-EX-10.24-COLLABORATION AGREEMENT (3).txt

**Cohort:** Revised prompt — final unseen set  
**Saved extraction started:** 15 Oct 2026 12:00:16 IST · **Model:** gemini-3.7-flash  
**Processing:** 14.042 seconds · **Recorded tokens:** 36272

[Source TXT](data/raw/contracts/final_validation_sample/XENCORINC_10_25_2013-EX-10.24-COLLABORATION%20AGREEMENT%20%283%29.txt)

| Field | Extracted | Reference as evaluated | Result |
| --- | --- | --- | --- |
| Parties | Xencor, Inc.<br>Boehringer Ingelheim International GmbH | Xencor, Inc<br>Boehringer Ingelheim International GmbH | Match |
| Agreement date | 2012-02-10 | 2/10/12 | Match |
| Governing law | State of New York, USA | New York | Mismatch |

**Date basis:** `defined_date`.

**Evidence presence:** 6/6 quotes found (whitespace-normalized).

**Review — governing_law (reference/evaluator):** Source expressly specifies State of New York, USA. Extraction retains USA while reference omits it. Same state, but the conservative comparator preserves country qualification and flags the string difference.

**Original CUAD parties answer:** Xencor, Inc ("XENCOR"); Boehringer Ingelheim International GmbH ("BII"); BII and XENCOR (each a “Party” and collectively “Parties”)

**Saved review reasons:**

- governing_law: Jurisdiction wording or scope differs; manual review required. Country and federal-law detail retained.

**Supporting quotes:**

- **parties:** This Collaboration Agreement ("Agreement") is made by and among     Xencor, Inc.
- **parties:** Boehringer Ingelheim International GmbH   Binger Straße 173 55216 Ingelheim Germany   (hereinafter called "BII")
- **agreement_date:** IN WITNESS WHEREOF, the Parties have caused this Agreement to be executed as of the Effective Date.
- **agreement_date:** 1.18 "Effective Date"   shall mean the date of commencement of this Agreement as mentioned on the cover page above.
- **agreement_date:** EFFECTIVE DATE: February 10, 2012
- **governing_law:** This Agreement shall be exclusively governed by and construed in accordance with the laws of the State of New York, USA without regard to its conflict of laws provisions.

## Milestone 2 closeout

Batch processing and evaluation are complete. Preserve these cases as regression/review examples when moving to PDF parsing. In particular, do not use a higher reference match rate as proof of correctness: stated-date versus signature-date policy, mixed collective descriptions, unnamed parties, affiliate scope and multi-jurisdiction wording remain explicit limitations. No further Gemini reruns or rule changes were performed to produce this consolidated report.
