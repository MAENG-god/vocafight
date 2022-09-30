from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from study.models import Vocas, Vocabulary
import random
from datetime import datetime

from study.views import vocabulary
# Create your views here.

def quiz(request):
    vocabularys = Vocabulary.objects.filter(author = request.user)
    template = loader.get_template('quiz/quiz.html')
    context = {
        "vocabularys":vocabularys,
    }
    return HttpResponse(template.render(context, request))

def quiz_all(request):
    vocas = Vocas.objects.filter(author = request.user)
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

def quiz_daily(request, id):
    vocabulary = Vocabulary.objects.get(id=id)
    vocas = Vocas.objects.filter(vocabulary=vocabulary)
    if vocas:
        random_num = random.randint(0, len(vocas) - 1)
        voca = vocas[random_num]
        context = {
            "vocas": vocas,
            "voca": voca,
            "id": id,
        }
    else:
        context = {
            "vocas": vocas,
        }
    
    template = loader.get_template('quiz/quiz_daily.html')
    return HttpResponse(template.render(context, request))  
