from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrationForm
from django.contrib.auth.decorators import login_required
from django.apps import apps

from budget import models as budget_models

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            budget_models.Category.create_default_categories(user)
            name = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {name}! You are logged in.')
            return redirect('dashboard')
    else:
        form = RegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profilepage(request):
    return render(request, 'users/profile.html')
