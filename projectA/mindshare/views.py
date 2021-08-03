from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from mindshare.models import Material
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
# from bincardcreation.serializers import materialserializers
from mindshare.forms import MaterialForm

def post_method(request):  
    if request.method == "POST":  
        form = MaterialForm(request.POST)  
        if form.is_valid():
            form.save()  
            return redirect('/display')  
    else:  
        form = MaterialForm() 
        context = {'form':form} 
    return render(request,'materials.html', context)  

def display(request):  
    materials = Material.objects.all()
    context = {'materials':materials} 
    return render(request,"display.html", context )  

def edit(request, receipt_no):  
    serializer = Material.objects.get(receipt_no=receipt_no) 
    context = {'Material':serializer} 
    return render(request,'Edit.html', context )  
def update(request, receipt_no):  
    serializer = Material.objects.get(receipt_no=receipt_no)  
    form = MaterialForm(request.POST, instance = serializer)  
    if form.is_valid():  
        form.save()
    messages.success(request,"Record Update sucessfully...")    
    return render(request, 'Edit.html', {'Material': serializer})  
def delete(request, receipt_no):  
    serializer = Material.objects.get(receipt_no=receipt_no)  
    serializer.delete()  
    return redirect("/display")




# Create your views here.
