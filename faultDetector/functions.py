import os
import sys
import pandas as pd
from io import StringIO

from faultDetector.Executor.runner import Runner


def check_csv(filename):
    # Expectd data types
    expected_dtypes = [object, int, float]

    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(filename, delimiter=";")

    # Check if the file is empty
    if df.empty:
        return False
        # raise ValueError("File is empty")
    
    # Check if the file has header row
    if df.columns[0] == 0:
        raise ValueError("File doesn't contain header rows")
    # Check number of column count
    if len(df.columns) != len(expected_dtypes):
        return False
        # raise ValueError("Column mismatch")
    
    # Check if the data types of each column match the expected data types
    for column, expected_dtype in zip(df.columns, expected_dtypes):
        actual_dtype = df[column].dtype
        if actual_dtype != expected_dtype:
            return False
            # raise ValueError(f"Expected type for column {column}: {expected_dtype.__name__}, actual dtype: {actual_dtype}")
     
   
    # Check for any missing or null values
    if df.isnull().values.any():
        return False
        # raise ValueError("CSV contains missing or null values")

    
    # If all checks pass, return True
    getMetadata(df)
    return True
   
def getMetadata(dataset):
    # Extract metadata of metadata
    df = pd.DataFrame(dataset)
    maxValue = round( df['Value'].max(), 2 )
    minValue = round( df['Value'].min(), 2 )
    avValue  = round( df['Value'].mean(),2 )


def runAlgorithms():
    PATH_ALGORITHM = "media/Algorithms"
    PATH_DATASET = "media/Datasets"
    algorithms = []
    datasets = []
    algorithm_files = [file for file in os.listdir(PATH_ALGORITHM) if file.endswith(".py")]

    for alg in algorithm_files:
        a = alg.replace('.py','')
        algorithms.append(a)
    for dataset in os.listdir(PATH_DATASET):
        datasets.append(dataset)

    Runner(algorithms, datasets)

