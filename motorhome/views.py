from django.shortcuts import render
from django.http import HttpResponse


def homepage(request):
    context = {"home_page": "active"}
    return render(request, 'motorhome/layout.html', context)

def about(request):
    context = {"about_page": "active"}
    return render(request, 'motorhome/about.html', context)

def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, 'motorhome/contacts.html', context)
