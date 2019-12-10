from django.shortcuts import render
from .models import Mentor, Blog, Mentee

# Create your views here.
def home(request):
    return render(request,"alta/home.html",{})
def mentor(request):
    mentors = Mentor.objects.all()
    return render(request,"alta/mentor.html",{"mentors": mentors})
def blog(request):
    blogs = Blog.objects.all()
    return render(request,"alta/blog.html",{"blogs": blogs})
def mentee(request):
    mentees = Mentee.objects.all()
    return render(request,"alta/mentee.html",{"mentees": mentees})
def author(request):
    return render(request,"alta/author.html",{})
def form(request):
    return render(request,"alta/form.html",{})
def submit(request):
    foto_blog = request.POST['foto']
    judul_blog = request.POST['judul']
    berita = request.POST['berita']

    new =Blog(foto_blog = foto_blog, judul_blog = judul_blog, berita = berita)
    new.save()

    blogs = Blog.objects.all()
    return render(request, 'alta/blog.html',{'blogs': blogs})