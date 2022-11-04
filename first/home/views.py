from django.shortcuts import render,HttpResponse
from home.models import servicemodule
def index(request):
    return render(request,"temp1.html")
    #return HttpResponse("this is my home page")
def about(request):
    return render(request,"about.html")
def login(request):
    return render(request,"html.html")
def service(request):
    if request.method =='POST':
        name=request.POST.get('name'),
        lname=request.POST.get('lname'),
        email=request.POST.get('email'),
        desc=request.POST.get('desc')
        service=servicemodule(name=name,lname=lname,email=email,desc=desc)
        service.save()
    return HttpResponse("this is my services page")

# Create your views here.
