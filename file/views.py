from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def fileupload(request):
    return render(request,'FileHandler1.html')