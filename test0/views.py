from django.shortcuts import render
from django.http import JsonResponse
from django.core.files.storage import default_storage
#from test0.Untitled8 import total_output
from django.contrib.auth import login
# Create your views here.
from json import dumps
from test0.models import diesease
from test0.deep import total_output,DISEASE_DIC

def index(request):
    
    return render(request, 'index.html')
def dry(request):
    
    return render(request, 'dry_skin.html')
def mix(request):
    
    return render(request, 'Mixed_skin.html')

def norm(request):
    
    return render(request, 'Normal_skin.html')

def oily(request):
    
    return render(request, 'Oily_skin.html')

def Herbal(request):
    
    return render(request, 'Herbal_page.html')

def skincare(request):
    
    return render(request, 'SkinCare_home.html')

def upload_image(request):
    
    return render(request, 'diagnose.html')
    
def result_image(request):
    path =default_storage.save("media/upload_images/"+request.FILES["files"].name,request.FILES["files"])
    p=total_output(path)
    print(path)
    if(p["data"]=='invalid image'):
        return render(request,'diagnose.html',{"error":"the image is not valid"})
    print(path)
    discript={}
    for i in range(4):
        pass
        try:
            d=diesease.objects.get(name=p["data"][i]["class_name"])
            discript[DISEASE_DIC[p["data"][i]["class_name"]]]=d.descript
        except:
            pass
        p["data"][i]["class_name"]=DISEASE_DIC[p["data"][i]["class_name"]]
    print(discript.keys())
    return render(request, 'results.html',{"discript":discript.items(),"dic1":dumps({"m":p}) })
