from django.shortcuts import render, HttpResponse


def myview(request):
    print("I am in view")
    return HttpResponse("This is home page")
