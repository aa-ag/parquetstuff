############ ------------ IMPORTS ------------##################################
import pandas as pd
import numpy as np
import pyarrow as pa


############ ------------ FUNCTION(S) ------------##############################
def read_applications():
    applications = pd.read_csv('inputdata/application_record.csv')
    applications = pd.concat(
        10*[applications]
    ).reset_index().drop(
        columns=['ID', 'index']
    ).reset_index().rename(
        columns={'index': 'ID'}
    )
    print(applications.head(5).T)


############ ------------ DRIVER CODE ------------##############################
if __name__ == "__main__":
    read_applications()
