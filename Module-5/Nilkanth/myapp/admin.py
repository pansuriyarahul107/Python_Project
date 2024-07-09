from django.contrib import admin
from .models import *

# Register your models here.
class manpowerDisplay(admin.ModelAdmin):
    list_display = ['uname','email','phone','age']


admin.site.register(manpower,manpowerDisplay)    