from typing import Optional

from .op_mapper import OpMapper
import pandas as pd
import phenopackets as PPkt
from importlib.resources import files


class OpUberonMapper(OpMapper):
    """
    A simple mapper for string representing anatomical locations to UBERON terms.
            
    UPDATE: January 28, 2025 
        - The primary_diagnosis_site appears to include lower case now (e.g. brain instead of Brain)

        - the site terms now match the UBERON preferred terms, so we don't need an extra step 
          going from the CDA site term to the UBERON preferred term.
        
    Results of using the column_values function as of January 28, 2025
    Command: sites = column_values(column='primary_diagnosis_site')
    mapping is in CDA_primary_diagnosis_site_to_uberon.csv (153 terms)

    """

    def __init__(self):
        """
        This is a simple map from the 'primary_diagnosis_site = row["primary_diagnosis_site"]' field of the diagnosis row

        Not sure how to deal with multiple sites that are listed in one entry
        
        1/29/25: _uberon_label_to_id and _site_to_uberon_label_d_orig are obsolete, leaving here for the moment...
        
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
            "Cervix Uteri": "uterine cervix",
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
        
        # directly go from site to uberon code
        #module_with_tissue_mapping_tables = 'oncopacket.ncit_mapping_files.cda_to_ncit_tissue_wise_mappings'
        #data_path = files(module_with_tissue_mapping_tables, tissue)    
        #    with open(data_path, 'r') as fh:
        #        df = pd.read_csv(
        #            fh,
        #            converters=CONVERTERS,
        #        )
        #    frames.append(df)
        module_with_tissue_mapping_tables = 'oncopacket.ncit_mapping_files'
        data_path = files(module_with_tissue_mapping_tables).joinpath("CDA_primary_diagnosis_site_to_uberon.csv")    
        with open(data_path, 'r') as fh:
                site_to_uberon = pd.read_csv(fh)
        #site_to_uberon = pd.read_csv("../src/oncopacket/ncit_mapping_files/CDA_primary_diagnosis_site_to_uberon.csv")
        self._site_to_uberon_code_d = dict(site_to_uberon.values)
        
    def get_ontology_term(self, row: pd.Series) -> Optional[PPkt.OntologyClass]:

        primary_site = row["primary_diagnosis_site"]

        if primary_site in self._site_to_uberon_code_d:
            # get standard label and UBEROBN id
            ontology_term = PPkt.OntologyClass()
            ontology_term.id = self._site_to_uberon_code_d.get(primary_site)
            ontology_term.label = primary_site
            return ontology_term
        else:
            # TODO -- more robust error handling in final release, but for development fail early
            raise ValueError(f"Could not find UBERON term for primary_site=\"{primary_site}\"")
        

