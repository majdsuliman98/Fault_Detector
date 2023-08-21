from django import forms


from .models import *

class DatasetForm(forms.ModelForm):
    class Meta:
        model = DatasetModel
        fields = ('name','file')

class AlgorithmForm(forms.ModelForm):
    class Meta:
        model = AlgorithmModel
        fields = ('name','description','sourceUrl')

class FaultRegistryForm(forms.ModelForm):
    class Meta:
        model = FaultRegistryModel
        fields = ('detectionAlgorithm','faultyRecord')


# class Result(forms.ModelForm):
#     class Meta:
#         model = AlgorithmModel
#         fields = ('executedAlgorithm','executedIteration','recordNumberIncluded','time')

        