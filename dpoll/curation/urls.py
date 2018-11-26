from django.urls import path

from . import views

urlpatterns = [
    path('blacklist/', views.index, name='black_list'),

]