from . import views
from django.urls import path

urlpatterns =[

    path('', views.basic, name='basic'),
    #path('add/', views.addition, name='addition'),

]