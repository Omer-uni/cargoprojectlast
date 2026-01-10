from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .models import Account


def register_view(request):
    if request.method == "POST":
        try:
            user = Account.objects.register(
                request.POST.get("username"),
                request.POST.get("email"),
                request.POST.get("password1"),
                request.POST.get("password2"),
            )
            login(request, user)
            return redirect("home")

        except ValidationError as e:
            return render(request, "register.html", {"error": e.message})

    return render(request, "register.html")


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("username"),
            password=request.POST.get("password"),
        )

        if user:
            login(request, user)
            return redirect("home")

        return render(request, "login.html", {
            "error": "Kullanıcı adı veya şifre hatalı"
        })

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login")
