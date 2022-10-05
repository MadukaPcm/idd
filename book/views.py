from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def BookView(request):
    
    context = {}
    return HttpResponse("books are here")

def RequestBookView(request):
    
    context = {}
    return HttpResponse("request book here")