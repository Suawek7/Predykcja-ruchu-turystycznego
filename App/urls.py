from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('result', views.result, name='result'),
    path('', views.index)
]