from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from study.models import Voca
import random
# Create your views here.

def quiz(request):
    vocas = Voca.objects.all()
    random_num = random.randint(0, len(vocas) - 1)
    voca = vocas[random_num]
    eng = voca.eng
    kor = voca.kor
    
    template = loader.get_template('quiz/quiz.html')
    context = {
        "eng": eng,
        "kor": kor,
    }
    return HttpResponse(template.render(context, request))
