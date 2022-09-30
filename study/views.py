from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Vocas, Vocabulary
from datetime import datetime
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required

def entrance(request):
    template = loader.get_template('study/entrance.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def study(request):
    template = loader.get_template('study/start.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))

def register(request):
    id = request.POST['id']
    vocabulary = Vocabulary.objects.get(id=id)
    voca = request.POST['voca']
    mean = request.POST['mean']
    Vocas.objects.create(vocabulary=vocabulary, author=request.user, eng=voca, kor=mean)
    return redirect("/study/vocabulary/" + str(id) + "/")
    
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
        vocabulary = Vocabulary.objects.create(author=request.user, name=name)
        return redirect('/study/vocabulary/' + str(vocabulary.id) + "/")
    else:      
        template = loader.get_template('study/create.html')
        context = {

        }
        return HttpResponse(template.render(context, request))

def vocabulary_create(request, id):
    template = loader.get_template('study/vocabulary_create.html')
    context = {
        "id": id
    }
    return HttpResponse(template.render(context, request))
    
def vocabulary_words(request, id):
    vocabulary = Vocabulary.objects.get(id=id)
    vocas = Vocas.objects.filter(vocabulary=vocabulary)
    template = loader.get_template('study/vocabulary_words.html')
    context = {
        "vocas":vocas,
    }
    return HttpResponse(template.render(context, request))