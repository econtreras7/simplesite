from unicodedata import name
from django.urls import  path
from .views import homePage


urlpatterns=[
    path("",homePage,name="home"),
]