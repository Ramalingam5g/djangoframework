from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from bincardcreation.models import Material
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib import messages
# from bincardcreation.serializers import materialserializers
from bincardcreation.forms import MaterialForm



# class MaterialView(APIView):

# def get(self,request):
#     material_list = material.objects.all()
#     serializer = materialserializers(material_list, many=True)
#     return render(request, "material.html", {"serializer":serializer.data})

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


    # def get(self,request):
    #     material_list = material.objects.all()
    #     serializer = materialserializers(material_list, many=True)
    #     return render(request, "material.html", {"serializer":serializer.data})

        
    # def post(self, request, format=None):
    #     serializer = materialserializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    

    # def post(self, request, format=None):
    #     material_list = material.objects.filter(receipt_no=request.POST['receipt_no'])
    #     serializer = materialserializers(material_list, many=True)
    #     return render(request, "material.html", {"serializer":serializer.data})
    
    
    # def put(self,request, receipt_no=None):
    #     #import pdb;pdb.set_trace()
    #     data=request.data
    #     obj=material.objects.filter(receipt_no=receipt_no)
    #     print(obj)
    #     putserializer=materialserializers(obj,data=data)
    #     if putserializer.is_valid():
    #         putserializer.save()
    #         return Response(putserializer.data, status=status.HTTP_201_CREATED)
    #     return Response(putserializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,receipt_no=None):
    #     obj=self.get_object(receipt_no)
    #     obj.delete()
    #     return Response(status=status.HTTP_200_OK)



# def user_data(request):
    # context = {
    # "date":"2021-07-20",
    # "doc_no":"20202",
    # "received_from":"sri ram industries",
    # "receipt_no":"102",
    # "issue":"ram industries",
    # "balance":"100",
    # "verification_date":"2020-01-11",
    # "verified_by":"ramalingam"

    # }
#     template_name="material.html"
#     return render(request, template_name, context)    

    
    # def post(self, request, format=None):
    #     serializer = materialserializers(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    # def get(self,request):
    #     material_list=material.objects.all()
    #     serializer = materialserializers(material_list,many=True)
    #     return Response(serializer.data)
    
    # def get_object(self,receipt_no):
    #     try:
    #         return material.objects.get(receipt_no=receipt_no)
    #     except material.DoesNotExist:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

    # # def get(self,request,receipt_no):
    # #     obj=self.get_object(receipt_no)
    # #     serializer = materialserializers(obj)
    # #     return Response(serializer.data)


    # def put(self,request,receipt_no=102):
    #     obj=self.get_object(receipt_no)
    #     putserializer=material(obj)
    #     if putserializer.is_valid():
    #         putserializer.save()
    #         return Response(putserializer.data, status=status.HTTP_201_CREATED)
    #     return Response(putserializer.error,status=status.HTTP_400_BAD_REQUEST)
    
    # def delete(self,request,receipt_no=102):
    #     obj=self.get_object(receipt_no)
    #     obj.delete()
    #     return Response(status=status.HTTP_200_OK)
        

    
    # def get(self,request):
    #     material_list=material.objects.all()
    #     serializer=materialserializers(material_list,many=True)
    #     return Response(serializer.data)
    
    # def get_object

# class Put_delete_method(APIView):

#     def get_object(self,receipt_no):
#         try:
#             return material.objects.get(receipt_no=receipt_no)
#         except material.DoesNotExist:
#             return Response(status=status.HTTP_400_BAD_REQUEST)

#     def get(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         serializer = materialserializers(obj)
#         return Response(serializer.data)

#     def put(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         putserializer=material(obj,data=request.data)
#         if putserializer.is_valid():
#             putserializer.save()
#             return Response(putserializer.data, status=status.HTTP_201_CREATED)
#         return Response(putserializer.error,status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self,request,receipt_no):
#         obj=self.get_object(receipt_no)
#         obj.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)






        
    
    
    





# Create your views here.
