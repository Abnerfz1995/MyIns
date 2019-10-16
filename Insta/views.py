from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from Insta.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from Insta.models import Post

#HelloWorld is-a TemplateView

class HelloWorld(TemplateView):
    template_name = "test.html"

class PostsView(ListView):
    #overwrite
    model = Post 
    template_name = "index.html"

class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post 
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post 
    template_name = "post_delete.html"
    success_url = reverse_lazy("posts")

class SignUp(CreateView):
    form_class =  CustomUserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")