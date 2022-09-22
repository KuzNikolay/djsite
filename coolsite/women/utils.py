from django.db.models import Count
from django.core.cache import cache
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        ]

class DataMixin:
    paginate_by = 2

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))
            cache.set('cats', cats, 50)


        user_menu = menu.copy() # если пользователь не авторизован не показывать "Добавить статью"
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = None # 0
        return context