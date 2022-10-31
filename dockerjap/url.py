from django.contrib import admin
from django.urls import path
from dockerjap import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.jk,name='jk'),
    path('index/',views.index,name="index"),
    # path('',views.img,name="img")   
]+static('static/') 