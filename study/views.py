from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Voca
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
    Voca.objects.create(eng=voca, kor=mean)
    return redirect("/")
    
def vocabulary(request):
    voca_dates = Voca.objects.all()
    dates = []
    for date in voca_dates:
        dates.append(date.today)
    dates = list(set(dates))
    template = loader.get_template('study/vocabulary.html')
    context = {
        "dates": dates
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
    vocas = Voca.objects.filter(today=date)
    template = loader.get_template('study/vocabulary_daily.html')
    context = {
        "vocas": vocas
    }
    return HttpResponse(template.render(context, request))
    