from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable":"I'm great"

    }
    return render(request,'index.html',context)
    

    # return HttpResponse("This is homepage")

def about(request):
    return render(request,'about.html')

def services(request):
    return request(request,'services.html')

def contact(request):
    return request(request,'contact.html')