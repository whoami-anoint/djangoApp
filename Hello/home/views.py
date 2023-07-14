from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is homepage")

def about(request):
    return HttpResponse("I am Abhishek Kafle")

def services(request):
    return HttpResponse("Bug bounty")