#@-4.What is Django URLs?make program to create django urls

''' 
In this article series on Django, we will learn what are URLs
and Views in Django. In Django, a URL is a unique string that 
represents a specific resource or action on a web application.

****** Creat django urls ******

from django.contrib import admin
from django.Urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("myapp.urls"))
]



'''