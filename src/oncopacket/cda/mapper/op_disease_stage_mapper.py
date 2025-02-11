from .op_mapper import OpMapper
from typing import Optional
import pandas as pd
import phenopackets as PPkt


class OpDiseaseStageMapper(OpMapper):

    def __init__(self):
        """
        This is a simple map from the 'stage' field of the diagnosis row
        """
        super().__init__(('stage',))

    def get_ontology_term(self, stage_str) -> Optional[PPkt.OntologyClass]:
        
        # changed passed variable from row (pandas series) to a string, because 
        # need to be able to submit a single term obtained from the GDC API, 
        # since the diagnoses.tumor_stage field, which 
        # CDA pulls, is empty in GDC for some reason
        
        #stage_str = row["stage"]

        ncit_label_to_id_d = {'Stage I': 'NCIT:C27966',
                            'Stage IA':'NCIT:C27975',
                            'Stage IB': 'NCIT:C27976',
                            'Stage II':'NCIT:C28054',
                            'Stage IIA':'NCIT:C27967',
                            'Stage IIB':'NCIT:C27968',
                            'Stage III':'NCIT:C27970',
                            'Stage IIIA': 'NCIT:C27977',
                            'Stage IIIB': 'NCIT:C27978',
                            'Stage IIIC1': 'NCIT:C95179',
                            'Stage IIIC2': 'NCIT:C95180',
                            'Stage IV': 'NCIT:C27971',
                            'Stage IVA': 'NCIT:C27979',
                            'Stage IVB': 'NCIT:C27972'
                            }
        
        stage_d = {'Stage I': 'Stage I',
                'Stage 1': 'Stage I',
                'stage I': 'Stage I',
                'stage 1': 'Stage I',
                'IA':'Stage IA',
                'Stage IA':'Stage IA',
                'stage IA':'Stage IA',
                'IB':'Stage IB',
                'Stage IB':'Stage IB',
                'stage IB':'Stage IB',
                'Stage II':'Stage II',
                'Stage 2':'Stage II',
                'stage 2':'Stage II',
                'stage II':'Stage II',
                'IIA':'Stage IIA',
                'Stage IIA':'Stage IIA',
                'stage IIA':'Stage IIA',
                'IIB':'Stage IIB',
                'Stage IIB':'Stage IIB',
                'stage IIB':'Stage IIB',
                'Stage 3':'Stage III',
                'stage 3':'Stage III',
                'Stage III':'Stage III',
                'stage III':'Stage III',
                'IIIA':'Stage IIIA',
                'Stage IIIA':'Stage IIIA',
                'Stage 3A':'Stage IIIA',
                'stage 3A':'Stage IIIA',
                'IIIB':'Stage IIIB',
                'Stage IIIB':'Stage IIIB',
                'Stage 3B':'Stage IIIB',
                'stage 3B':'Stage IIIB',
                'Stage IIIC1': 'Stage IIIC1',
                'Stage IIIC2': 'Stage IIIC2',
                'IV':'Stage IV',
                'Stage 4':'Stage IV',
                'Stage IV':'Stage IV',
                'stage IV':'Stage IV',
                'Stage IVA': 'Stage IVA',
                'Stage IVB': 'Stage IVB'
                }
        
        ontology_term = PPkt.OntologyClass()
        
        #print("stage_str: " + stage_str)
        if stage_str in stage_d:
            # get standard label and NCIT id
            stage_label = stage_d.get(stage_str)
            stage_id = ncit_label_to_id_d.get(stage_label)
            ontology_term.id = stage_id
            ontology_term.label = stage_label
        else:
            ontology_term.id ='NCIT:C92207'  # Stage unknown
            ontology_term.label = 'Stage Unknown'
            
        return ontology_term

'''
All stages in CDA
stages = column_values(column='stage')

	stage	count
0		117106
1	III	503
2	Stage IIA	410
3	Stage IIIC	346
4	Stage II	189
5	Stage IIIA	169
6	Stage IIB	159
7	Stage IIIB	141
8	Stage IA	117
9	Stage I	113
10	IV	103
11	Stage IV	93
12	M0	92
13	IA	88
14	Stage III	87
15	T2N0M0	64
16	IB	63
17	II	62
18	M3	52
19	Stage IB	41
20	IIIa	40
21	Stage1	28
22	Stage IVA	21
23	M1	20
24	T3N0M0	17
25	IIIA	16
26	IIb	13
27	IIA	8
28	Ia	8
29	M2	8
30	Stage IC	8
31	IVa	7
32	Not Received	5
33	T2N1M0	5
34	pT3a	5
35	V	4
36	Va	4
37	IVb	3
38	Not Performed	3
39	T3N0M1	3
40	I	2
41	IIB	2
42	T2N0M1	2
43	T3N1M0	2
44	IIIB	1
45	IIIb	1
46	T2N1M1	1
47	T2N2M1	1
48	T3N1M1	1
49	TisN1M1	1
50	Vb	1
51	pT1	1
52	pT1a	1
53	pT1b	1
54	pT4	1
'''