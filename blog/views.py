from django.shortcuts import render

from .models import Blog

def allblogs(request):
	allblogposts = Blog.objects
	return render(request, 'blog/allblogs.html',{'allblogposts':allblogposts})