from django.shortcuts import render
from blog.models import BlogContent
# Create your views here.


def signup(request):
    res  = render(request,'signup.html')
    return res

def signin(request):
    res = render(request,'login.html')
    return res 


def blogpageOne(request,slug):
    post = BlogContent.objects.filter(slug = slug).first()
    # print(post)
    context = {
        'post':post
    }
    res = render(request,'blogpost.html',context)
    return res




def blogpage(request):
    allposts = BlogContent.objects.all()
    print(allposts)
    context={
        'allposts':allposts,
    }
    res = render(request,'blogpage.html',context)
    return res 


def home(request):
    res = render(request,'home.html')
    return res