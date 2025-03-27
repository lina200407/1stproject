from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    
    context ={
        'projects' : Project.objects.all(),
        'abouttext' : About.objects.last(),
        'contactme' : ContactInfo.objects.last(),
    }
    return render(request,'pages/index.html', context)
