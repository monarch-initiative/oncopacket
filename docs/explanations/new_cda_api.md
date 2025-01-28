# Explanation of the new CDA API
New API implemented 4/10/24

From the CDA:

To merge multiple tables, add the subject_id column to both the researchsubject and diagnosis tables them merge them with the subject table:
 
    research = fetch_rows(table='researchsubject', add_columns=['subject_id'])
    diag = fetch_rows(table='diagnosis', add_columns=['subject_id'])
    sub = sub.merge(research, on='subject_id', how='outer')
    sub = sub.merge(diag, on='subject_id', how='outer')
 
Note that this produces multiple rows for subjects if they have multiple diagnosis_ids which is common in the PDC data.
 
### Data sources

The source repository can included in a data_source column with the addition of a provenance=True argument:
 
    sub = fetch_rows(table='subject', provenance=True)
 
The caveat is that if provenance is added to a table, add_columns cannot be used also. Another point is that a data_source_id column will be created as well which produces multiple rows when the record is found in multiple sources.
 
So if you add the provenance to subjects:
 
    sub = fetch_rows(table='subject', provenance=True)
 
then subject_data_source and subject_data_source_id will be added. You can then get the researchsubject and diagnosis tables and add the subject_id:
 
    research = fetch_rows(table='researchsubject', add_columns=['subject_id'])
    diag = fetch_rows(table='diagnosis', add_columns=['subject_id'])
 
and do the merge. You can also add the provenance to the researchsubject table:
 
    sub = fetch_rows(table='subject', add_columns=['researchsubject_id'])
    research = fetch_rows(table='researchsubject', provenance=True)
    diag = fetch_rows(table='diagnosis', add_columns=['researchsubject_id'])
 
or the diagnosis table:
 
    sub = fetch_rows(table='subject', add_columns=['diagnosis_id'])
    research = fetch_rows(table='researchsubject', add_columns=['diagnosis_id'])
    diag = fetch_rows(table='diagnosis', provenance=True)
 
In this last case, some subjects do not have diagnosis records, so those subjects are excluded.
 
To avoid the merge expanding each subject into many more rows, consolidate the data_source_id columns (or just delete it). For example, for subject provenance:
 
    sub['subject_data_source_id_concat'] = sub.groupby(['subject_id','subject_data_source'])['subject_data_source_id'].transform(lambda x: ','.join(x))
    sub = sub.drop(columns=['subject_data_source_id'], axis=1)
    sub = sub.drop_duplicates()
 
 ### GDC diagnosis.tumor_stage

 The GDC data here:
 
https://portal.gdc.cancer.gov/analysis_page?app=CohortBuilder&tab=stage_classification
 
is available through the GDC API but it is not clearly described in the documentation. 
diagnoses.tumor_stage does not return any data. However, using the schema document here:
 
https://github.com/NCI-GDC/gdcdictionary/blob/develop/src/gdcdictionary/schemas/diagnosis.yaml
 
endpoints such as diagnoses.ajcc_pathologic_stage, diagnoses.ajcc_clinical_stage, diagnoses.ann_arbor_pathologic_stage, and diagnoses.ann_arbor_clinical_stage can be constructed. 
 
For the CDA data team, reconciling different stage data from different systems is fraught with issues and not in their current scope. They query the tumor_stage endpoint only, which has no data.
 
With regards to vital status, use the demographic.vital_status endpoint. 