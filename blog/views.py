from django.shortcuts import render, get_object_or_404

from .models import Blog

def allblogs(request):
	allblogposts = Blog.objects
	return render(request, 'blog/allblogs.html',{'allblogposts':allblogposts})

def detail(request,blog_id):
	detailblog = get_object_or_404(Blog,pk=blog_id)
	return render(request, 'blog/detail.html', {"detailblog":detailblog})