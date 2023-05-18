############ ------------ IMPORTS ------------##################################
import pandas as pd
import numpy as np
import pyarrow as pa


############ ------------ FUNCTION(S) ------------##############################
def read_applications_doc():
    applications = pd.read_csv('data/application_record.csv')
    applications = pd.concat(
        10*[applications]
    ).reset_index().drop(
        columns=['ID', 'index']
    ).reset_index().rename(
        columns={'index': 'ID'}
    )
    return applications


def extract_schema(applications_data):
    doc_schema = pa.Schema.from_pandas(applications_data)
    return doc_schema


def convert_csv_to_parquet():
    applications_data = read_applications_doc()
    applications_doc_schema = extract_schema(applications_data)
    applications_data.to_parquet(
        'data/applications_processed.parquet',
        schema=applications_doc_schema
    )


############ ------------ DRIVER CODE ------------##############################
if __name__ == "__main__":
    convert_csv_to_parquet()
