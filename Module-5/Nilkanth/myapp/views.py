from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def index (request):
    userdata = manpower.objects.all()
    return render(request,"index.html",{"userdata":userdata})

def addmanpower(request):
    if request.method=='POST':
        id = request.POST['id']
        uname = request.POST['uname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']

        if id == "":

            manpower.objects.create(uname=uname,email=email,phone=phone,age=age)
        else:
            udata = manpower.objects.get(id = id) 
            udata.uname = uname 
            udata.email = email
            udata.phone = phone
            udata.age = age
            udata.save()

        return redirect("index")    
     
def delete(request,id):
        userdata = manpower.objects.get(id=id)
        userdata.delete()
        
        return redirect("index") 


def edit(request,id):
        user = manpower.objects.get(id=id)
        userdata = manpower.objects.all()
        
        
        
        return render(request,"index.html",{"data":user,"userdata":userdata})         
