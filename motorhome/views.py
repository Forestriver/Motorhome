from django.shortcuts import render
from django.http import HttpResponse

def index(response):
    return HttpResponse('Hi! The front page will be created later today.')

# Create your views here.
