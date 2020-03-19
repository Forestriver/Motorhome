from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    context = {"home_page": "active"}
    return render(request, 'motorhome/homepage.html', context)

def about(request):
    context = {"about_page": "active"}
    return render(request, 'motorhome/about.html', context)

def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, 'motorhome/contacts.html', context)

def login(request):
    context = {"login_page": "active"}
    return render(request, 'motorhome/admin.py', context)
