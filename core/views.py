from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# Create your views here.
def signup(request):
    if request.method == "POST":
        usname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        r_password = request.POST.get("repeat_password")
        if password != r_password:
            return render(request, "core/signup.html", {
                "error" : "Пароли не совпадают"
            })
        User.objects.create_user(
            username = usname,
            email = email,
            password = password,
        )
        return redirect("signin")
    return render(request, "core/auth/signup.html")


def signin(request):
    return render(request, "core/auth/signin.html")


def profile(request):
    return render(request, "core/auth/profile.html")


def signout(request):
    pass