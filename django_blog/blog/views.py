from django.shortcuts import render, redirect
from django.http import request, redire
from .forms import UserRegisteration
from .models import Post

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


def register(request):
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegisteration()
        return  render(request, 'auth/register.html', {'form' : form})

class BlogListView(ListView):
    model = Post
    fields = "__all _"

class BlogDetailView(DetailView):
    model = Post
    fields = "__all _"

class BlogCreateView(CreateView):
    model = Post
    fields = "__all _"

class BlogUpdateView(UpdateView):
    model = Post
    fields = "__all _"

class BlogDeleteView(DeleteView):
    model = Post
    fields = "__all _"