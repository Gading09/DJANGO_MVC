from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('mentor', views.mentor, name = 'mentor'),
    path('blog', views.blog, name = 'blog'),
    path('mentee', views.mentee, name = 'mentee'),
    path('author', views.author, name = 'author'),
    path('blog/input', views.form, name = 'form'),
    path('blog/submit',views.submit,name='submit')
]