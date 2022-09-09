from django.urls import path, re_path

from women.views import *


urlpatterns = [
    path('', index, name='home'), # http://127.0.0.1:8000/
    # path('cats/<int:catid>/', categories),# http://127.0.0.1:8000/cats/catid
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive), # http://127.0.0.1:8000/archive/2022
    path('about/', about, name='about'), # http://127.0.0.1:8000/about/
]