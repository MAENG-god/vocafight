from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from study.models import Vocas, Vocabulary
import random
from datetime import datetime
# Create your views here.

def quiz(request):
    voca_dates = Vocas.objects.all()
    dates = []
    for date in voca_dates:
        dates.append(date.today)
    dates = list(set(dates))
    print(dates)
    template = loader.get_template('quiz/quiz.html')
    context = {
        "dates": dates
    }
    return HttpResponse(template.render(context, request))

def quiz_all(request):
    vocas = Vocas.objects.all()
    random_num = random.randint(0, len(vocas) - 1)
    voca = vocas[random_num]
    eng = voca.eng
    kor = voca.kor
    
    template = loader.get_template('quiz/quiz_all.html')
    context = {
        "eng": eng,
        "kor": kor,
    }
    return HttpResponse(template.render(context, request))

def quiz_daily(request, date):
    date_url = date
    months = [None, "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    date = date.split()
    date[1] = date[1].replace(',', '')
    date[0] = str(months.index(date[0][0:3]))
    date[0] = date[0].zfill(2)
    date = date[2] + "-" + date[0] + "-" + date[1]
    date_format = "%Y-%m-%d"
    date = datetime.strptime(date, date_format)
    vocas = Vocas.objects.filter(today=date)
    random_num = random.randint(0, len(vocas) - 1)
    voca = vocas[random_num]
    eng = voca.eng
    kor = voca.kor
    
    template = loader.get_template('quiz/quiz_daily.html')
    context = {
        "eng": eng,
        "kor": kor,
        "date": date_url,
    }
    return HttpResponse(template.render(context, request))  
