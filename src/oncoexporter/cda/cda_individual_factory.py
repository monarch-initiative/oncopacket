import phenopackets as PPkt
import pandas as pd

from ..model.op_Individual import OpIndividual
from src.oncoexporter.cda.mapper.op_mapper import OpMapper
from .cda_factory import CdaFactory

class CdaIndividualFactory(CdaFactory):
    """
    Create GA4GH individual messages from other data sources. Each data source performs ETL to
    create an instance of the OpIndivual class and then returns a GA4GH Individual object.
    """
    def __init__(self, op_mapper=None) -> None:
        """
        :param OpMapper: An object that is able to map free text to Ontology terns
        """
        super().__init__()
        if op_mapper is None:
            self._opMapper = OpMapper()
        else:
            self._opMapper = op_mapper

    @staticmethod
    def days_to_iso(days: int):
        """
        Convert the number of days of life into an ISO 8601 period representing the age of an individual
        (e.g., P42Y7M is 42 years and 7 months).
        # FYI this exists:
        # https://pypi.org/project/iso8601/

        :param days: number of days of life (str or int)
        """
        if isinstance(days, str):
            days = int(str)
        if not isinstance(days, int):
            raise ValueError(f"days argument must be int or str but was {type(days)}")
        # slight simplification
        days_in_year = 365.2425
        y = int(days/days_in_year)
        days = days - int(y*days_in_year)
        m = int(days/12)
        days = days - int(m*12)
        w = int(days/7)
        days = days - int(w*7)
        d = days
        iso = "P"
        if y > 0:
            iso = f"{iso}{y}Y"
        if m > 0:
            iso = f"{iso}{m}M"
        if w > 0:
            iso = f"{iso}{w}W"
        if d > 0:
            iso = f"{iso}{d}D"
        return iso


    @staticmethod
    def days_to_iso(days:int):
        """
        Convert the number of days of life into an ISO 8601 period representing the age of an individual
        (e.g., P42Y7M is 42 years and 7 months).
        # FYI this exists:
        # https://pypi.org/project/iso8601/

        :param days: number of days of life (str or int)
        """
        if isinstance(days, str):
            days = int(str)
        if not isinstance(days, int):
            raise ValueError(f"days argument must be int or str but was {type(days)}")
        # slight simplification
        days_in_year = 365.2425
        y = int(days/days_in_year)
        days = days - int(y*days_in_year)
        m = int(days/30.437)
        # average number of days in a month: 30.437
        days = days - int(m*30.437)
        w = int(days/7)
        days = days - int(w*7)
        d = days
        iso = "P"
        if y > 0:
            iso = f"{iso}{y}Y"
        if m > 0:
            iso = f"{iso}{m}M"
        """
        if w > 0:
            iso = f"{iso}{w}W"
        if d > 0:
            iso = f"{iso}{d}D"
        """
        return iso


    def process_vital_status(self, row):
        """
        :param vital_status: "Alive or Dead"
        :type vital_status: str
        :param days_to_death: 
        """
        vital_status = self.get_item(row, "vital_status")
        days_to_death = self.get_item(row, "days_to_death")
        cause_of_death = self.get_item(row, "cause_of_death") 
        if vital_status is None:
            return None 
        valid_status = {"Alive", "Dead"}
        if vital_status not in valid_status:
            return None
        vstatus = PPkt.VitalStatus()
        if vital_status == "Alive":
            vstatus.status = PPkt.VitalStatus.ALIVE
        elif vital_status == "Dead":
            vstatus.status = PPkt.VitalStatus.DECEASED
        if days_to_death is not None:
            try:
                dtd = int(days_to_death)
                vstatus.survival_time_in_days = dtd
            except:
                pass
        cause = self._opMapper.get_nci_term(cause_of_death)
        if cause is not None:
            vstatus.cause_of_death.CopyFrom(cause)
        return vstatus

    def from_cancer_data_aggregator(self, row):
        """
        convert a row from the CDA subject table into an Individual message (GA4GH Phenopacket Schema)
        The row is a pd.core.series.Series and contains the columns
        ['subject_id', 'subject_identifier', 'species', 'sex', 'race',
       'ethnicity', 'days_to_birth', 'subject_associated_project',
       'vital_status', 'days_to_death', 'cause_of_death']
       :param row: a row from the CDA subject table
        """
        if not isinstance(row, pd.core.series.Series):
            raise ValueError(f"Invalid argument. Expected pandas series but got {type(row)}")
        row = row.astype(str)
        subject_id = row['subject_id']
        subject_identifier = row['subject_identifier']
        species = row['species']
        sex = row['sex']
        race = row['race']
        ethnicity = row['ethnicity']
        days_to_birth = row['days_to_birth']
        # a valid date looks like this: '-15987.0'
        if days_to_birth.startswith("-"):
            days_to_birth = days_to_birth[1:]
        iso_age = None
        vstat = None
        try:
            # we need to parse '15987.0' first as a float and then transform to int
            d_to_b = int(float(days_to_birth))
            iso_age = CdaIndividualFactory.days_to_iso(days=d_to_b)
            vstat = self.process_vital_status(row)
        except:
            pass
        subject_associated_project = row['subject_associated_project']

        # status_object = process_vital_status(row)
        #
        # if status_object is not None:
        #     vital_status = status_object.vital_status
        #     days_to_death = status_object.days_to_death
        #     cause_of_death = status_object.cause_of_death

        # TODO figure out where to store project data
        opi = OpIndividual(id=subject_id, iso8601duration=iso_age, sex=sex, vital_status=vstat, taxonomy=species)
        return opi.to_ga4gh()