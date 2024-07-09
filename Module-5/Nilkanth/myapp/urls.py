
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path("",index,name= "index"),
    path("addmanpower/",addmanpower,name="addmanpower"),
    path("delete/<id>",delete,name="delete"),
    path("edit/<id>",edit,name="edit")
    
]
