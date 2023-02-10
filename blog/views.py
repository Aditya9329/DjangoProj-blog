from django.shortcuts import render

# Create your views here.


def signup(request):
    res  = render(request,'signup.html')
    return res

def signin(request):
    res = render(request,'login.html')
    return res 

def blogpage(request):
    res = render(request,'blogpage.html')
    return res 