from django.shortcuts import render
from django.http import HttpResponse

def index():
    return render(request, 'layout.html', {})

def about(request):
    return render(request, 'motorhome/about.html', {})

def admin(request):
    return render(request, 'motorhome/admin.html', {})

def contacts(request):
    return render(request, 'motorhome/contacts.html', {})

def homepage(request):
    return render(request, 'motorhome/homepage.html', {})
