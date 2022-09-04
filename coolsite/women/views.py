from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request):
    return HttpResponse("<title>Категории</title><h1>Статьи по категориям</h1>")
