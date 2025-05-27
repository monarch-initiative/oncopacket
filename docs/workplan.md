# Project Overview

Oncopacket is a Python library designed to harmonize genetic and clinical cancer data from the National Cancer Institute (NCI) into [GA4GH Phenopackets](https://phenopacket-schema.readthedocs.io/en/latest/), an ISO standard for representing clinical case data.

## Goals and Objectives

The primary goal of Oncopacket is to facilitate the integration of cancer research data by:

1. Converting data from the Cancer Research Data Commons (CRDC) to the GA4GH Phenopacket Schema
2. Enabling downstream analysis using a standardized data format
3. Creating a foundation for interoperability with other data sources

## Related Projects

The [pyphetools](https://github.com/monarch-initiative/pyphetools) project has a comparable code base targeted at rare disease, while Oncopacket focuses specifically on cancer data.

## Data Sources

Oncopacket currently uses:

1. The [Cancer Data Aggregator (CDA) API](https://github.com/CancerDataAggregator/cdapython) to access most cancer data elements
2. Direct access to the [Genomic Data Commons (GDC) API](https://gdc.cancer.gov/access-data/gdc-application-programming-interface-api) for specific elements like variant data, cancer stage, and vital status

## Project Status and Components

Oncopacket transforms clinical and genomic data from 12 different cancer types into standardized Phenopackets. The current implementation includes:

| Component | Description | Status |
|:----------|:------------|:-------|
| [CdaIndividualFactory](./cda/cda_individual_factory.md) | Converts subject data to Individual objects | Complete |
| [CdaDiseaseFactory](./cda/cda_disease_factory.md) | Converts diagnosis data to Disease objects | Complete |
| [CdaBiosampleFactory](./cda/cda_biosample_factory.md) | Handles biological sample data | Complete |
| [CdaMutationFactory](./cda/cda_mutation_factory.md) | Transforms mutation/variant data | Complete |
| [CdaMedicalactionFactory](./cda/cda_medicalaction_factory.md) | Processes interventions and treatments | Complete |

## Current Accomplishments

Oncopacket has been used to generate phenopackets for 23,650 individuals across 12 cancer types, with 7,816 of those having detailed mutational data. These datasets are available in a [Zenodo repository](https://doi.org/10.5281/zenodo.14610228).

## Future Directions

Future development efforts include:

1. Extending the code to incorporate more data elements from CRDC
2. Adding support for additional external data sources beyond NCI
3. Enhancing the mapping capabilities for oncology terms and concepts
4. Developing more comprehensive analysis tools that leverage the phenopacket format

## Project Tracking

The development is tracked on the [Oncopacket GitHub Project Board](https://github.com/orgs/monarch-initiative/projects/60/views/1){:target="_blank"}.

The code repository is available at [GitHub](https://github.com/monarch-initiative/oncopacket){:target="_blank"}.

