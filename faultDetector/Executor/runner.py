from multiprocessing import Process
from .main import runAnalysis

def Runner(algorithms, datasets):
    process = Process(target=runAnalysis, args=(algorithms, datasets))
    process.start()
    process.join()
