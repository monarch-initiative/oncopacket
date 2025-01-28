from typing import Optional

from .op_mapper import OpMapper
import pandas as pd
import phenopackets as PPkt


class OpUberonMapper(OpMapper):
    """
    A simple mapper for string representing anatomical locations to UBERON terms.
    UPDATE: January 28, 2025 
        - The primary_diagnosis_site appears to include lower case now (e.g. brain instead of Brain)
        
    TODO -- replace this with file based version covering all of the strings we need in CDA
    """

    def __init__(self):
        """
        This is a simple map from the 'primary_diagnosis_site = row["primary_diagnosis_site"]' field of the diagnosis row
        
        Not sure how to deal with multiple sites that are listed in one entry
        """
        super().__init__(('primary_diagnosis_site',))
        self._uberon_label_to_id = {
            'lung': 'UBERON:0002048',
            'endocervix': "UBERON:0000458",
            "uterine cervix": "UBERON:0000002",
            "uterus": "UBERON:0000995",
            "body of uterus": "UBERON:0009853",
            "lower respiratory tract": "UBERON:0001558",
            'breast': 'UBERON:0000310',
            'bone marrow': 'UBERON:0002371',
            'bone': 'UBERON:0002481',
            'brain': 'UBERON:0000955',
            'colon': 'UBERON:0001155',
            'heart': 'UBERON:0000948',
            'kidney': 'UBERON:0002113',
            'adrenal gland': 'UBERON:0002369',
            'liver': 'UBERON:0002107',
            'pancreas': 'UBERON:0001264',
            'skin': 'UBERON:0002097',
            'thyroid gland': 'UBERON:0002046'
        }
        self._site_to_uberon_label_d = {
            "abdomen, arm, bladder, chest, Head-Neck, Kidney, Leg, Retroperitoneum, Stomach, Uterus": "uterus",
            "Lung": "lung",
            "Lung, NOS": "lung",
            "cervix uteri": "uterine cervix",
            "cervix Uteri": "uterine cervix",
            "cervix Uteri, Unknown": "uterine cervix",
            "cervix": "uterine cervix",
            "Endocervix": "endocervix",
            "Uterus, NOS": "uterus",
            "corpus uteri": "body of uterus",
            "corpus Uteri": "body of uterus",
            "corpus Uteri, Unknown": "body of uterus",
            "Uterus": "uterus",
            "bronchus and lung": "lower respiratory tract",
            "bronchus and Lung": "lower respiratory tract",
            "Lower lobe, lung": "lower respiratory tract",
            "Overlapping lesion of lung": "lower respiratory tract",
            "Lung/bronchus": "lower respiratory tract",
            "Lung/bronchus, Unknown": "lower respiratory tract",
            "breast": "breast", 
            "breast, NOS": "breast",
            "breast, Unknown": "breast",
            "bone marrow": "bone marrow", 
            "bone Marrow": "bone marrow",
            "bones, joints and articular cartilage of other and unspecified sites": "bone",
            "bones, joints and articular cartilage of limbs": "bone",
            "bones of skull and face and associated joints (excludes mandible C41.1)": "bone",
            "Long bones of lower limb and associated joints": "bone",
            "Long bones of upper limb, scapula and  associated joints": 'bone',
            "Pelvic bones, sacrum, coccyx and associated joints": "bone",
            "bone, NOS" : 'bone',
            "bone": "bone",
            "bones": "bone",
            "brain": "brain",
            "brain, NOS": "brain",
            "brain, Unknown": "brain",
            "Overlapping lesion of brain and central nervous system": "brain",
            "Overlapping lesion of brain": "brain",
            "brain stem": "brain",
            "Colon": "colon",
            "Colon, NOS": "colon",
            "Colon, Unknown": "colon",
            "Heart, mediastinum, and pleura": "heart",
            "Connective, subcutaneous and other soft tissues of thorax (excludes thymus C37.9, heart and mediastinum C38._)": "heart",
            "Kidney": "kidney",
            "Kidney, NOS": "kidney",
            "Kidney, Unknown": "kidney",
            "Renal pelvis": "kidney",
            "Renal Pelvis": "kidney",
            "adrenal gland": "adrenal gland",
            "adrenal Gland": "adrenal gland",
            "adrenal gland, NOS": "adrenal gland",
            "adrenal gland, Unknown": "adrenal gland",
            "Liver and intrahepatic bile ducts": "liver",
            "Liver": "liver",
            "Intrahepatic bile ducts": "liver",
            "Pancreas": "pancreas",
            "Pancreas, NOS": "pancreas",
            "Pancreas, Unknown": "pancreas",
            "Pancreatic duct": "pancreas",
            "Skin": "skin",
            "Skin, NOS": "skin",
            "Skin, Unknown": "skin",
            "Connective, subcutaneous and other soft tissues": "skin",
            "Connective, subcutaneous and other soft tissues of pelvis": "skin",
            "Connective, subcutaneous and other soft tissues of lower limb and hip": "skin",
            "Connective, subcutaneous and other soft tissues, NOS": "skin",
            "Connective, subcutaneous and other soft tissues of upper limb and shoulder": "skin",
            "Connective, subcutaneous and other soft tissues of head, face, and neck (excludes connective tissue of orbit C69.6 and nasal cartilage C30.0)": "skin",
            "Skin of scalp and neck": "skin",
            "Skin of lower limb and hip": "skin",
            "Connective, subcutaneous and other soft tissues of abdomen": "skin",
            "Connective, subcutaneous and other soft tissues of trunk, NOS": "skin",
            "Skin, NOS (excludes skin of labia majora C51.0, skin of vulva C51.9, skin of penis C60.9 and skin of scrotum C63.2)": "skin",
            "Thyroid gland": "thyroid gland",
            "Thyroid Gland": "thyroid gland",
            "Thyroid gland, NOS": "thyroid gland",
            "Thyroid gland, Unknown": "thyroid gland",
            "Thyroid Gland, Unknown": "thyroid gland",
        }

    def get_ontology_term(self, row: pd.Series) -> Optional[PPkt.OntologyClass]:
        primary_site = row["primary_diagnosis_site"]


        if primary_site in self._site_to_uberon_label_d:
            # get standard label and UBEROBN id
            ontology_term = PPkt.OntologyClass()
            ontology_term.id = self._uberon_label_to_id.get(self._site_to_uberon_label_d.get(primary_site))
            ontology_term.label = self._site_to_uberon_label_d.get(primary_site)
            return ontology_term
        else:
            # TODO -- more robust error handling in final release, but for development fail early
            raise ValueError(f"Could not find UBERON term for primary_site=\"{primary_site}\"")
        
'''
Results of using the column_values function as of January 28, 2025
Command: sites = column_values(column='primary_diagnosis_site')

primary_diagnosis_site	count
	66419
chest	28221
breast	21203
lung	12289
immune system	9029
brain	6383
kidney	5085
colon	4676
ovary	3893
prostate gland	3284
pancreas	2931
uterus	2547
thyroid gland	1715
stomach	1577
skin of body	1464
lymph node	1207
uterine cervix	1080
hepatobiliary system	1070
adrenal gland	1068
craniocervical region	1023
central nervous system	978
liver	956
body of uterus	951
esophagus	876
rectum	618
testis	465
thoracic cavity element	388
ear	368
upper esophagus	346
appendicular skeleton	325
thymus	315
hypodermis	293
limb bone	256
pelvic region of trunk	246
sublingual gland	221
larynx	166
digestive system	153
gallbladder	149
nervous system	143
abdomen	142
tongue	137
cerebellum	133
head	128
female reproductive organ	106
intestine	97
biliary system	92
eye	90
rectosigmoid junction	90
anal canal	81
nasopharynx	71
urinary bladder	71
small intestine	70
bone tissue	69
brainstem	66
mouth	62
renal system	57
spinal cord	57
mouth floor	56
bile duct	51
limb	51
cardiac ventricle	48
tonsil	48
frontal lobe	46
temporal lobe	39
posterior part of tongue	28
parietal lobe	23
pineal tract	23
telencephalon	22
orbit of skull	21
hindlimb	16
oropharynx	16
vagina	16
ureter	15
mammary gland	13
penis	13
endocrine gland	12
mammalian vulva	12
nasal cavity	12
parotid gland	12
gingiva	11
occipital lobe	11
blood	10
upper limb segment	10
hypopharynx	9
lip	9
trachea	9
meningeal cluster	8
thoracic segment of trunk	8
inguinal lymph node	7
renal pelvis	7
retina	7
pituitary gland	6
roof of mouth	6
hindlimb long bone	5
mandible	5
skin of hip	5
cranium	4
eyelid	4
facial lymph node	4
lower lobe of lung	4
peritoneum	4
scrotum	4
bone of pelvis	3
mediastinum	3
middle ear	3
optic disc	3
pleura	3
posterior mediastinum	3
vermiform appendix	3
vertebral column	3
adrenal cortex	2
alimentary part of gastrointestinal system	2
anterior mediastinum	2
axial skeleton plus cranial skeleton	2
bone marrow	2
endocervix	2
ethmoid sinus	2
head or neck skin	2
male reproductive system	2
multicellular organism	2
pharynx	2
respiratory system	2
soft palate	2
spleen	2
tail of pancreas	2
thoracic skeleton	2
urethra	2
axillary lymph node	1
buccal mucosa	1
caecum	1
chest wall	1
cranial nerve	1
craniopharyngeal canal	1
duodenum	1
epididymis	1
fallopian tube	1
forelimb nerve	1
forelimb skin	1
hard palate	1
head of pancreas	1
heart	1
jejunum	1
lateral wall of nasopharynx	1
maxillary sinus	1
meninx of spinal cord	1
pancreatic duct	1
paranasal sinus	1
pleural cavity	1
shoulder	1
sigmoid colon	1
skin of trunk	1
submandibular gland	1
supraglottic part of larynx	1
urachus	1
'''
