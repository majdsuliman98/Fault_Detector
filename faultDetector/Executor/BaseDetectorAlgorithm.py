from abc import abstractmethod

class BaseDetectorAlgorithm:

    def __init__(self, algorithmName) -> None:
        if algorithmName is None or len(algorithmName) < 1:
            raise Exception("Child Algorithm didn't init Super Class")
        self.algorithmName = algorithmName
    
    @abstractmethod
    def read(self):
        exceptionMessage = "Read method not implemented in algorithm - " + self.algorithmName
        raise Exception(exceptionMessage)

    @abstractmethod
    def detect(self):
        exceptionMessage = "Detect method not implemented in algorithm - " + self.algorithmName
        raise Exception(exceptionMessage)
    
    @abstractmethod
    def writeback(self):
        exceptionMessage = "Writeback method not implemented in algorithm - " + self.algorithmName
        raise Exception(exceptionMessage)
    
