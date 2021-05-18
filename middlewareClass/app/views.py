from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse


def myview(request):
    print("I am in view")
    return HttpResponse("This is home page")

def exception_view(request):
    raise ValueError(12/0)
    return HttpResponse("This is the process_exception view")

def process_template_view(request):
    context = {'title': 'Sasmal'}
    return TemplateResponse(request,'app/index.html', context)
