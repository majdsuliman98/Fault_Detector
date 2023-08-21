from django.shortcuts import render,redirect,reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.contrib import messages
from .forms import *
from .functions import *
from .models import *


def home(request):
    
    return render(request,'home.html')

def addAlgorithm(request):
    if request.method == 'POST':

        data = request.FILES['file'] 
        filename = request.POST['fileName']
        description = request.POST['description']
        if(len(description) == 0):
                description = "None"
        
        path = default_storage.save(f"Algorithms/{filename}.py",ContentFile(data.read()))
        fdata = {"name": filename, "description": description, "sourceUrl": path}
        form = AlgorithmForm(fdata)
        # print(form.has_error(field='description'))
        if form.is_valid():


            model = form.save(commit=False)
            model.save()
            runAlgorithms()



        return JsonResponse({'message': 'File uploaded successfully.'})
    return render(request,'addAlgorithm.html')

def reports(request):
    return render(request,'reports.html')

def loadingScreen(request):
    return render(request,'loadingScreen.html')

def updateDataset(request):

    if request.method == 'POST':
        data = request.FILES['file'] 
        filename = request.POST['fileName']
        filepath = f"Datasets/{filename}.csv"
        path = default_storage.save(filepath,ContentFile(data.read()))

        # Check wether CSV file is valid 
        if check_csv(f"./media/{filepath}"):
            messages.success(request, "File is valid")
            fdata = {"name": filename, "file": path}
            form = DatasetForm(fdata)

            if form.is_valid():
                model = form.save(commit=False)
                model.save()
                
            # runAlgorithms()
            return redirect('loading')

        else:
            default_storage.delete(filepath)
            messages.error(request, "File is invalid")

        
      ## Issue persists trying to display message to user
        # return redirect('see_reports')
    else:
        return render(request, 'updateDataset.html')


def information(request):
    datasets = DatasetModel.objects.all()
    algorithms = AlgorithmModel.objects.all()
    context = {
        "datasets": datasets,
        "algorithms": algorithms,
    }
    return render(request,'information.html',context)