# Using the Cancer Data Aggregator (CDA) API

This document explains how Oncopacket interacts with the Cancer Data Aggregator (CDA) API to extract cancer research data and transform it into GA4GH Phenopackets.

## Overview of CDA API Integration

Oncopacket utilizes the CDA Python library (`cdapython`) to access data from the NCI Cancer Research Data Commons. The CDA provides a unified API that aggregates data from multiple NCI data repositories, including:

- Genomic Data Commons (GDC)
- Proteomic Data Commons (PDC)
- Imaging Data Commons (IDC)
- Clinical Trial Data Commons (CTDC)

## Accessing Specific Data Elements

### Cancer Stage Information

While CDA's `diagnoses.tumor_stage` endpoint doesn't return data, Oncopacket directly accesses GDC API endpoints for cancer staging information:

- `diagnoses.ajcc_pathologic_stage`
- `diagnoses.ajcc_clinical_stage`
- `diagnoses.ann_arbor_pathologic_stage`
- `diagnoses.ann_arbor_clinical_stage`

These endpoints are constructed based on the GDC schema document: https://github.com/NCI-GDC/gdcdictionary/blob/develop/src/gdcdictionary/schemas/diagnosis.yaml

### Vital Status Information

For vital status, Oncopacket uses the `demographic.vital_status` endpoint.

## Data Transformation Process

1. **Extract**: Fetch data from CDA tables
2. **Transform**: Convert CDA data models to Oncopacket model classes
3. **Map**: Use ontology mappers to standardize terminology
4. **Load**: Populate GA4GH Phenopacket structures

The CDA factory classes in Oncopacket handle these transformation processes, creating a streamlined pipeline from CDA data to standardized phenopackets.

## Updates and Changes

**Note**: This documentation reflects the CDA API implementation as of April 10, 2024. As the CDA API evolves, Oncopacket's interaction with it may change.
