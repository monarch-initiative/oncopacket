# CdaFactory

The `CdaFactory` class serves as a base class for the various factory classes that transform Cancer Data Aggregator (CDA) data into components of GA4GH Phenopackets.

## Overview

This abstract factory class provides common functionality for its concrete subclasses:
- `CdaIndividualFactory`: Transforms subject data into Individual objects
- `CdaDiseaseFactory`: Transforms diagnosis data into Disease objects
- `CdaBiosampleFactory`: Transforms specimen/sample data into Biosample objects
- `CdaMutationFactory`: Transforms mutation data into Variant objects

## API Documentation

::: src.oncopacket.cda.CdaFactory
