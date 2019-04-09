from django.shortcuts import render, HttpResponse
from some_name.models import Blog

# Create your views here.

def about(request):
	return HttpResponse("About Page")

def contactus(req):
	return render(req,'contact.html',{})

def home(request):
	return render(request, 'home.html', {'blogs':Blog.objects.all()})

def detail(request, blog_id):
	blog = Blog.objects.get(id=blog_id)
	return render(request,'detail.html', {'blog':blog})