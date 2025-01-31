# README downloaded_files
This directory is where we download certain files from the web. The code only downloads the files once, because we
assume that they are static within the time course of using this package. To override this, call the corresponing
"load" methods with overwrite=True.

We have added the file Neoplasm_Core.tsv to the repository. This file was downloaded on Jan 14, 2024, from
https://ncit.nci.nih.gov/ncitbrowser/ajax?action=values&vsd_uri=http://evs.nci.nih.gov/valueset/C126659#, representing

NCIt Neoplasm Core Terminology (http://evs.nci.nih.gov/valueset/C126659) and is useful for generating lists of synonyms.

UBERON_Terminology.csv comes from https://evs.nci.nih.gov/ftp1/UBERON/About.html (downloaded 1/28/25).  It has the following fields:

|Spreadsheet Column	| Content Description |
|-------------------|---------------------|
|Subset Code|	The NCIt concept code attached to the subset concept. NCIt Codes are unique strings that begin with a C and are followed by a series of digits.|
|Subset Term|	The name of the terminology subset.|
|NCIt Concept Code|	The NCIt concept code attached to the NCIt concept that has been mapped to an UBERON concept.|
|NCIt Preferred Term|	The term chosen by NCI EVS subject matter expert that unambiguously describes the concept.|
|NCIt Definition|	A text definition of the term created by an NCI EVS subject matter expert.|
|UBERON Code|	The concept code provided by UBERON. UBERON codes are unique strings that begin with UBERON: followed by seven digits.|
|UBERON Preferred Term|	The label for the concept as provided by UBERON.|
|UBERON Synonym(s)|	Terms provided by UBERON that are exact synonyms for the UBERON label (UBERON Preferred Term).|
|UBERON Definition|	A textual description for the concept provided by UBERON.|
