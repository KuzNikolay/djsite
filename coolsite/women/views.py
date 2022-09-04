from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{cat}</p>")
