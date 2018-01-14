# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from login_account.forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import NewsForm,Post
from django.core.urlresolvers import reverse_lazy

def hello(request):
    number=[1,2,3,4,5]
    name="Sandeep Chauhan"
    args = {'myname':name,'Number':number}
    return render(request, 'login_account/home.html', args)

def register(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/login/login_account')
	else:
		form = RegistrationForm()
	args = {'form': form}
	return render (request,'login_account/reg_form.html',args)
@login_required
def profile(request):
	args = {'user': request.user}
	return render (request,'login_account/profile.html',args)

@login_required
def edit_profile(request):
	if request.method == "POST":
		form = EditProfileForm(request.POST, instance = request.user)
		if form.is_valid():
			form.save()
			return redirect('/login/profile')
	else:
		form = EditProfileForm(instance = request.user)
		args = {'form': form}
		return render (request,'login_account/edit_profile.html',args)

@login_required
def public_page(request):
	number=[1,2,3,4,5]
	name="Sandeep Chauhan"
	args = {'myname':name,'Number':number}
	return render (request,'login_account/public_page.html', args)


class BlogListView(ListView):
	model = Post
	template_name = 'login_account/post_list.html'


def post_detail(request,*args, **kwargs):
	blog_post = get_object_or_404(Post, pk=kwargs.get("pk"))
	if blog_post.author == request.user:
		
		return render(request,'login_account/post_detail.html',{'post':blog_post})
	else:
		return redirect('/login/public_page/')
		

@login_required	
def news_poster(request):
    if request.method == 'POST':
        
        form = NewsForm(request.POST)
        if form.is_valid():
            news_item = form.save(commit = False)
            news_item.author = request.user  # User posting the form
            news_item.save()
        return redirect('/login/public_page/')
    else:
        form = NewsForm()
    return render(request,'login_account/post_new.html', {'form': form})



    

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'text']
    template_name = 'login_account/post_edit.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'login_account/post_delete.html'
    success_url = reverse_lazy('post_list') 
# Create your views here.
