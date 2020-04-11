from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    context = {"main_page": "active"}
    return render(request, 'motorhome/main.html', context)

def services(request):
    context = {"services_page": "active"}
    return render(request, 'motorhome/services.html', context)

def technologies(request):
    context = {"technologies_page": "active"}
    return render(request, 'motorhome/technologies.html', context)

def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, 'motorhome/contacts.html', context)
