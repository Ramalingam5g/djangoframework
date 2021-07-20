from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bincardcreation.models import material

class Myview(View):
    
    def get(self,request):
        #materials=material.object.all()
        
        return HttpResponse('get the values')
    
    def post(self,request):
        
        return HttpResponse('values to be posted')
    
    def delete(self,request):

        return HttpResponse("values to be deleted")

    
    





# Create your views here.
