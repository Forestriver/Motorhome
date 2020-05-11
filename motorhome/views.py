from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def main(request):
    context = {"main_page": "active"}
    return render(request, 'main.html', context)

def services(request):
    context = {"services_page": "active"}
    return render(request, 'services.html', context)

def technologies(request):
    context = {"technologies_page": "active"}
    return render(request, 'technologies.html', context)

def contacts(request):
    context = {"contacts_page": "active"}
    return render(request, 'contacts.html', context)

def ping(request):
    data = {'ping':"pong"}
    return JsonRequest(data)
