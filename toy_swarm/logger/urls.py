# logger/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('log', views.log_message, name='message_logger'),
]