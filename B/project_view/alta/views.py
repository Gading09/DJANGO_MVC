from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"alta/home.html",{})
def mentor(request):
    return render(request,"alta/mentor.html",{})
def blog(request):
    return render(request,"alta/blog.html",{})
def mentee(request):
    return render(request,"alta/mentee.html",{})
def author(request):
    return render(request,"alta/author.html",{})