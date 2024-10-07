from django.shortcuts import render


def index(request):
    render(request, "index.html")


def login(request):
    render(request, "login.html")


def logout(request):
    render(request, "index.html")
