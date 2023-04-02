from django.urls import path
from . import views

urlpatterns = [
  path('getpost/', views.telegram_bot, name='telegram_bot'),
  path('', views.index, name='index')

]