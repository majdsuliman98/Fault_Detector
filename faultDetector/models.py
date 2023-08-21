from django.db import models
from django.utils import timezone
    
class DatasetModel(models.Model):
    name = models.CharField(max_length=45)
    file = models.CharField(max_length=45)
    date = models.DateTimeField(default=timezone.now)
    # id = models.AutoField(primary_key=True)  # Add an AutoField as primary key

    class Meta:
        db_table = "SourceDataset"

class AlgorithmModel(models.Model):
    name = models.CharField(max_length=45, primary_key=True)
    description = models.CharField(max_length=45)
    sourceUrl = models.CharField(max_length=256)
    date = models.DateTimeField(default=timezone.now)

        
    class Meta:
        db_table = "Algorithm"

class ResultsModel(models.Model):
    executedAlgorithm = models.CharField(max_length=45)
    executedIteration = models.IntegerField()
    recordNumberIncluded = models.BigIntegerField
    time = models.DateTimeField(default=timezone.now)

        
    class Meta:
        db_table = "Results"
class FaultRegistryModel(models.Model):
    detectionAlgorithm = models.CharField(max_length=45)
    faultyRecord = models.IntegerField()
    class Meta:
        db_table = "faultRegistry"
