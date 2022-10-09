from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from study.models import Vocas, Vocabulary
import random
from django.contrib.auth.decorators import login_required
from study.views import vocabulary
# Create your views here.

@login_required
def quiz(request):
    vocabularys = Vocabulary.objects.filter(author = request.user)
    template = loader.get_template('quiz/quiz.html')
    context = {
        "vocabularys":vocabularys,
    }
    return HttpResponse(template.render(context, request))

@login_required
def quiz_all(request):
    vocas = Vocas.objects.filter(author = request.user)
    if vocas:
        random_num = random.randint(0, len(vocas) - 1)
        voca = vocas[random_num]
        if len(voca.kor) >= 2:
            firstKor = voca.kor[0]
            secondKor = voca.kor[0:2]
        else:
            firstKor, secondKor = "단어가 너무 짧거나 없음", "단어가 너무 짧거나 없음"
        context = {
            "vocas": vocas,
            "voca": voca,
            "id": id,
            "firstKor": firstKor,
            "secondKor": secondKor,
        }
    else:
        context = {
            "vocas": vocas,
        }
    template = loader.get_template('quiz/quiz_all.html')
    return HttpResponse(template.render(context, request))

vocas = None
@login_required
def start(request):
    global vocas
    if request.POST:
        vocabularyIds = request.POST.getlist("id")
        vocabularyIds = list(map(int, vocabularyIds))
        vocabularys = Vocabulary.objects.filter(id__in=vocabularyIds)
        print(vocabularys)
        vocas = Vocas.objects.filter(vocabulary__in=vocabularys)
        if vocas:
            random_num = random.randint(0, len(vocas) - 1)
            voca = vocas[random_num]
            if len(voca.kor) >= 2:
                firstKor = voca.kor[0]
                secondKor = voca.kor[0:2]
            else:
                firstKor, secondKor = "단어가 너무 짧거나 없음", "단어가 너무 짧거나 없음"
            context = {
                "vocas": vocas,
                "voca": voca,
                "firstKor": firstKor,
                "secondKor": secondKor,
            }
        else:
            context = {
                "vocas": vocas,
            }
        print(vocas)
        template = loader.get_template('quiz/quiz_all.html')
        return HttpResponse(template.render(context, request))
    else:
        if vocas:
            random_num = random.randint(0, len(vocas) - 1)
            voca = vocas[random_num]
            if len(voca.kor) >= 2:
                firstKor = voca.kor[0]
                secondKor = voca.kor[0:2]
            else:
                firstKor, secondKor = "단어가 너무 짧거나 없음", "단어가 너무 짧거나 없음"
            context = {
                "vocas": vocas,
                "voca": voca,
                "firstKor": firstKor,
                "secondKor": secondKor,
            }
        else:
            context = {
                "vocas": vocas,
            }
        template = loader.get_template('quiz/quiz_all.html')
        return HttpResponse(template.render(context, request))
        
