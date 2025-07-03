# csv_cleaner.py
import pandas as pd
from dagster import op, job

@op
def load_csv():
    df = pd.read_csv("data.csv")
    print("\nOriginal Data:\n", df)
    return df

@op
def clean_csv(df: pd.DataFrame):
    cleaned_df = df.dropna()
    print("\nCleaned Data:\n", cleaned_df)
    return cleaned_df

@op
def save_csv(df: pd.DataFrame):
    df.to_csv("cleaned_data.csv", index=False)
    print("\nSaved to cleaned_data.csv")

@job
def csv_cleaning_job():
    save_csv(clean_csv(load_csv()))
