from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from datetime import datetime
from .models import Post
from .forms import PostCreateForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

    
def index(request):
	return HttpResponse("hello world, This is chandu")

def current_datetime(request):
	return HttpResponse("<html><body>it is now %s.</body></html>" %datetime.now())

def post_list(request):
	posts = Post.objects.all()
	context = {
		'posts': posts,
	}
	return render(request, 'blog/post_list.html', context)

def post_detail(request, id, slug):
	post = get_object_or_404(Post, id=id, slug=slug)
	context = {
		'post': post,
	}
	return render(request, 'blog/post_detail.html', context)

def getinput(request):
	return render(request, 'blog/getinput.html')

def postinput(request):
	return render(request, 'blog/postinput.html')

def add(request):
	if request.method == "GET":
		try:
			a=request.GET['t1']
			x=int(a)
			b=request.GET['t2']
			y=int(b)
			z=x+y
			return HttpResponse("<html><body bgcolor=red><h1>sum is: "+str(z)+"</h1></body></html>")

		except(ValueError):
			return HttpResponse("Invalid input")
	else:
		if request.method == "POST":
			try:
				a=request.POST['t1']
				x=int(a)
				b=request.POST['t2']
				y=int(b)
				z=x+y
				return HttpResponse("<html><body bgcolor=red><h1>sum is: "+str(z)+"</h1></body></html>")

			except(ValueError):
				return HttpResponse("Invalid input")

def post_create(request):
	if request.method == 'POST':
		form = PostCreateForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.save()
	else:		
		form = PostCreateForm()
	context = {
		'form': form,
	}
	return render(request, 'blog/post_create.html', context)


def user_login(request):
	if request.method == 'POST':
		form = UserLoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user:
				if user.is_active:
					login(request, user)
					return redirect("post_list")
				else:
					return HttpResponse("User is not active")
			else:
				return HttpResponse("User is none")
	else:
		form = UserLoginForm()

		context = {
			'form': form,
		}
		return render(request, 'blog/login.html', context)

def user_logout(request):
	logout(request)
	return redirect('post_list')