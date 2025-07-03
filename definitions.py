# definitions.py
from dagster import Definitions
from csv_cleaner import csv_cleaning_job

defs = Definitions(
    jobs=[csv_cleaning_job]
)
