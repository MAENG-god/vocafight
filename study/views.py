from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Voca

# Create your views here.

def study(request):
    template = loader.get_template('study/study.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def register(request):
    voca = request.POST['voca']
    mean = request.POST['mean']
    Voca.objects.create(eng=voca, kor=mean)
    return redirect("/")
    