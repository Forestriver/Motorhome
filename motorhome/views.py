from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return render(response, 'motorhome/layout.html')
