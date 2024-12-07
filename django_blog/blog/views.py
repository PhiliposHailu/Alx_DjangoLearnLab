from django.shortcuts import render, redirect
from django.http import request, redire
from .forms import UserRegisteration


def register(request):
    if request.method == 'POST':
        form = UserRegisteration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            form = UserRegisteration()
        return  render(request, 'auth/register.html', {'form' : form})
    
def profile(request):
    return render(request, 'blog/profile.html')