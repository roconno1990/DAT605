#views.py
from project.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import RequestContext
from project.models import Post
from django.core.paginator import Paginator
 
@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
 
    return render(request, 'registration/register.html', {'form' : form})

def register_success(request):
    return render(request, 'registration/success.html')
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')
 
@login_required
def home(request):
    post_list = Post.objects.all()
    paginator = Paginator(post_list, 1)

    return render(request, 'home.html', {'posts' : post_list})

def single(request, single):
    single = Post.objects.get(id=single)
    context = {
        'post' : single, 
    }
    return render(request, 'single.html', context)
