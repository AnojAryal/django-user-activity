from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse("This is Home page of application")
    return render(request, "index.html")


def about(request):
    return HttpResponse("This is About page of application")


def services(request):
    return HttpResponse("This is Services page of application")


def contact(request):
    return HttpResponse("This is Contact page of application")
