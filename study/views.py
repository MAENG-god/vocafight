from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Vocas, Vocabulary
from datetime import datetime

# Create your views here.

def study(request):
    template = loader.get_template('study/study.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def register(request):
    voca = request.POST['voca']
    mean = request.POST['mean']
    Vocas.objects.create(eng=voca, kor=mean)
    return redirect("/")
    
def vocabulary(request):
    vocabularys = Vocabulary.objects.all()

    template = loader.get_template('study/vocabulary.html')
    context = {
        "vocabularys":vocabularys,
    }
    return HttpResponse(template.render(context, request))

def createvocabulary(request):
    if request.POST:
        name = request.POST['name']
        Vocabulary.objects.create(author=request.user, name=name)
        return redirect('/study/vocabulary/')
    else:      
        template = loader.get_template('study/create.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

def vocabulary_daily(request, date):
    months = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date = date.split()
    date[1] = date[1].replace(',', '')
    date[0] = str(months.index(date[0][0:3]))
    date[0] = date[0].zfill(2)
    date = date[2] + "-" + date[0] + "-" + date[1]
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date, date_format)
    vocas = Vocas.objects.filter(today=date)
    template = loader.get_template('study/vocabulary_daily.html')
    context = {
        "vocas": vocas
    }
    return HttpResponse(template.render(context, request))
    