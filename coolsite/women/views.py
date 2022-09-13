from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
        ]


def index(request):
    posts = Women.objects.all()

    context_index = {
        'posts': posts,
        'menu': menu,
        'title': 'Главная страница',
        'cat_selected': 0,
        }
    return render(request, 'women/index.html', context = context_index)

def about(request):
    return render(request, 'women/about.html', {'menu': menu, 'title': 'О Сайте'})

def addpage(request):
    return HttpResponse("Добавление статьи")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Авторизация")

def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")

def pageNotFaund(request, exception):
    return HttpResponseNotFound(f'<h1>Страница не найдена</h1><p>СОВСЕМ НЕ НАЙДЕНА</p>')

def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context_index = {
        'posts': posts,
        'menu': menu,
        'title': f'Категория: {cat_id}',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context_index)
