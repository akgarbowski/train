from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def ann(request):
    return HttpResponse("Hello, world. You're at polls index.")

def calvin(request, num1:int, num2:int):
    return HttpResponse(f"Hello, your sum is! \n {num1+num2}")

