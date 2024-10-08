from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, "index.html")


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check for user credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return render(
                request, "login.html", {"error": "Invalid username or password"}
            )

    return render(request, "login.html")


def logoutUser(request):
    logout(request)
    return redirect("/login")
