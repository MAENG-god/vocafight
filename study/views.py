from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Vocas, Vocabulary, Vocabulary_example, Vocabulary_example_deleted, Vocas_example
from django.contrib.auth.decorators import login_required 

# Create your views here.

def help(request):
    user = request.user
    template = loader.get_template('study/help.html')
    context = {
        "user":user,
    }
    return HttpResponse(template.render(context, request))    

@login_required
def information(request):
    userName = request.user
    template = loader.get_template('study/information.html')
    context = {
        "userName": userName,
    }
    return HttpResponse(template.render(context, request))

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

@login_required
def register(request):
    id = request.POST['id']
    vocabulary = Vocabulary.objects.get(id=id)
    voca = request.POST['voca']
    mean = request.POST['mean']
    Vocas.objects.create(vocabulary=vocabulary, author=request.user, eng=voca, kor=mean)
    return redirect("/study/vocabulary/" + str(id) + "/")
    
@login_required
def vocabulary(request):
    exampleVocabularys = Vocabulary_example.objects.all()
    examples_deleted = Vocabulary_example_deleted.objects.filter(user=request.user)
    if examples_deleted:
        exampleList = []
    else:
        exampleList = exampleVocabularys
             
    
    vocabularys = Vocabulary.objects.filter(author=request.user)

    template = loader.get_template('study/vocabulary.html')
    context = {
        "vocabularys":vocabularys,
        "exampleVocabularys": exampleList,
    }
    return HttpResponse(template.render(context, request))

@login_required
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

@login_required
def example(request):
    vocabulary = Vocabulary_example.objects.all()
    vocas = Vocas_example.objects.all()
    template = loader.get_template('study/vocabulary_example.html')
    context = {
        "vocabulary": vocabulary,
        "vocas": vocas,
    }
    return HttpResponse(template.render(context, request))

@login_required
def example_delete(request):
    Vocabulary_example_deleted.objects.create(user=request.user)
    return redirect("/study/vocabulary/")

@login_required
def vocabulary_create(request, id):
    vocabulary = Vocabulary.objects.get(author=request.user, id=id)
    if request.POST:
        vocabulary.name = request.POST["vocabularyName"]
        vocabulary.save()
        return redirect("/study/vocabulary/{}/".format(id))
    else:
        template = loader.get_template('study/vocabulary_create.html')
        context = {
            "id": id,
            "vocabulary": vocabulary,
        }
        return HttpResponse(template.render(context, request))
    
@login_required
def vocabulary_words(request, id):
    vocabulary = Vocabulary.objects.get(id=id)
    vocas = Vocas.objects.filter(vocabulary=vocabulary)
    template = loader.get_template('study/vocabulary_words.html')
    context = {
        "vocas":vocas,
        "id": id,
    }
    return HttpResponse(template.render(context, request))

@login_required
def vocabulary_delete(request, id):
    vocabulary = Vocabulary.objects.get(author=request.user, id=id)
    vocabulary.delete()
    return redirect("/study/vocabulary/") 

@login_required
def vocabulary_words_delete(request, vocabulary_id, voca_id):
    voca = Vocas.objects.get(author=request.user, id=voca_id)
    voca.delete()
    return redirect("/study/vocabulary/words/" + str(vocabulary_id) + "/")

@login_required
def vocabulary_words_edit(request, vocabulary_id, voca_id):
    voca = Vocas.objects.get(author=request.user, id=voca_id)
    voca.eng = request.POST['eng']
    voca.kor = request.POST['kor']
    voca.save()
    return redirect("/study/vocabulary/words/" + str(vocabulary_id) + "/")

@login_required
def deleteUser(request):
    user = request.user
    user.delete()
    return redirect("/accounts/logout/")
