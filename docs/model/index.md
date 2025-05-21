# Oncopacket: Model Module

The *model* module of Oncopacket contains data models that represent cancer patient data. 
These models can be constructed with data from various upstream sources and then exported in GA4GH Phenopacket format.

## Core Classes

The model module includes several key classes:

### OpIndividual

The `OpIndividual` class represents a cancer patient, with demographic information, disease diagnoses, biosamples, and genetic variants.

[API Documentation for OpIndividual](./op_individual.md)

### OpDisease

The `OpDisease` class represents cancer diagnoses, including cancer type, stage, grade, and other diagnostic information.

### OpMutation

The `OpMutation` class represents genetic mutations/variants found in a patient's tumor samples.

## Usage Example

```python
from oncopacket.model import OpIndividual
import phenopackets as PPkt

# Create vital status object
vital_status = PPkt.VitalStatus()
vital_status.status = PPkt.VitalStatus.ALIVE

# Create an individual
individual = OpIndividual(
    id="TCGA-12345",
    sex="FEMALE",
    iso8601duration="P65Y",  # 65 years old
    vital_status=vital_status
)

# Convert to GA4GH Phenopacket Individual
ga4gh_individual = individual.to_ga4gh()
```

Note that the `to_ga4gh()` method only converts the individual information to a GA4GH format. For creating complete phenopackets with disease and mutation information, you should use the factory classes provided in the CDA module.

## Integration with CDA

The model classes are populated by the factory classes in the CDA module, which 
extract data from the Cancer Data Aggregator API and convert it to the appropriate 
model objects.

