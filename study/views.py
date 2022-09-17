from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def study(request):
    template = loader.get_template('study/study.html')
    context = {
        
    }
    return HttpResponse(template.render(context, request))