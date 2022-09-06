from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения Women")

def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")

def archive(request, year):
    if int(year) > 2022:
        return redirect('home', permanent=True)
    return HttpResponse(f"<h1>Архв по годам</h1><p>{year}</p>")

def pageNotFaund(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><p>СОВСЕМ НЕ НАЙДЕНА</p>')