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
    template_name = 'blog/list_posts.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog/details_of_posts.html'

class BlogCreateView(CreateView):
    model = Post
    fields = "__all _"
    template_name = 'blog/create_update.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = "__all _"
    template_name = 'blog/create_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
