from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from bincardcreation.models import material
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from bincardcreation.serializers import materialserializers

class bincardtable(APIView):
    
    def post(self, request, format=None):
        serializer = materialserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def get(self,request):
        material_list=material.objects.all()
        serializer=materialserializers(material_list,many=True)
        return Response(serializer.data)

class materilaserializers(APIView):

    def get_objet(self,receipt_no):
        try:
            return material.objects.get(receipt_no=receipt_no)
        except material.DoesNotExist:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request,receipt_no):
        obj=self.get_objet(receipt_no)
        serializer = materialserializers(obj)
        return Response(serializer.data)

    def put(self,request,receipt_no):
        obj=self.get_objet(receipt_no)
        putserializer=material(obj,data=request.data)
        if putserializer.is_valid():
            putserializer.save()
            return Response(putserializer.data, status=status.HTTP_201_CREATED)
        return Response(putserializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,receipt_no):
        obj=self.get_objet(receipt_no)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




        
    
    
    





# Create your views here.
