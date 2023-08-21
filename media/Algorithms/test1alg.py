
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import importlib.util

current_dir = os.path.dirname(os.path.abspath(__file__))  # Get the absolute path of the current directory
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))  # Go one directory up
grandparent_dir = os.path.abspath(os.path.join(parent_dir, '..'))  # Go one directory up again
executor_dir = os.path.join(grandparent_dir, 'faultDetector', 'Executor')  # Create the path to the 'executor' directory
script_path= f"{executor_dir}/BaseDetectorAlgorithm.py"
spec = importlib.util.spec_from_file_location('BaseDetectorAlgorithm', script_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

BaseDetectorAlgorithm = module.BaseDetectorAlgorithm




class FaultDetectorSigma(BaseDetectorAlgorithm):

    def __init__(self) -> None:
        super().__init__("Algorithm B")
        #Algorith Setup

    def read(self,dataset):
        print("before")
        self.df = pd.read_csv(dataset, sep = ";", parse_dates=['Timestamp'])
        self.detect()
        print("done")

    
    def detect(self):
        Over_by_4_sigma = self.df.Value.mean() + (4 * self.df.Value.std())
        Under_by_4_sigma = self.df.Value.mean() - (4 * self.df.Value.std())
        self.df["Outside"] = np.where((self.df.Value < Over_by_4_sigma) & (self.df.Value > Under_by_4_sigma), False, True)
        self.issues_df = self.df[self.df['Outside'] == True]
        print("detect done")
    
    def writeback(self):
        return self.issues_df
    



def getAlgorithmClassName():
    return "FaultDetectorSigma"