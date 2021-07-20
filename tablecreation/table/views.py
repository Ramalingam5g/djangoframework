from django.shortcuts import render
from django.http import HttpResponse

def display(request):
    message='<h1> table created </h1>'
    return  HttpResponse(message)

