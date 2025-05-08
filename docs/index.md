# Oncopacket

Oncopacket is a Python library designed to harmonize genetic and clinical cancer data 
into [GA4GH Phenopackets](https://github.com/phenopackets/phenopacket-schema){:target="\_blank"}, an ISO standard for representing 
clinical case data. This library enables interoperability and standardized data 
representation for cancer genomics research.

Oncopacket transforms cancer data into the GA4GH Phenopacket Schema, facilitating integration with 
upstream cancer data sources and downstream analytical tools. Currently, Oncopacket primarily uses 
the [Cancer Data Aggregator (CDA)](https://datacommons.cancer.gov/cancer-data-aggregator){:target="\_blank"} Python library to extract cohorts 
from NCI's Cancer Research Data Commons (CRDC).

## Core Features

- **Data Integration**: Extracts demographic, mutation, morphology, diagnosis, intervention, and survival data from NCI cancer data
- **Data Standardization**: Converts cancer data to GA4GH Phenopackets format
- **Ontology Mapping**: Maps cancer terms to standardized ontologies like NCIT and UBERON
- **Analysis Support**: Enables downstream cohort analysis, survival studies, and other statistical/ML applications

## Main Components

- **CDA Module**: Factories and importers to transform CDA data into phenopacket components
- **Model Module**: Core data structures representing individuals, diseases, and genetic mutations
- **Mapping Tools**: Utilities to map between different oncology terminologies

## Getting Started

To get started with Oncopacket, follow these steps:

1. [Install Oncopacket](installation.md)
2. See our examples in the [Jupyter notebooks](https://github.com/monarch-initiative/oncopacket/tree/main/notebooks)
3. Explore the [API documentation](model/index.md)

## Project Status

While Oncopacket currently focuses on data from NCI's Cancer Research Data Commons, the 
modular code can be extended for use with other data sources. The software is designed 
to accurately represent existing data from upstream sources without imputing missing 
records.

## Feedback

The best place to leave feedback, ask questions, and report bugs is the
[Oncopacket Issue Tracker](https://github.com/monarch-initiative/oncopacket/issues){:target="\_blank"}.

