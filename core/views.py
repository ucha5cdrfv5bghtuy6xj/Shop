from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signup(request):
    if request.method == "POST":
        usname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        r_password = request.POST.get("repeat_password")
        if password and email and r_password and usname:
            if password != r_password:
                return render(request, "core/auth/signup.html", {
                    "error" : "Пароли не совпадают"
                })
            user = User.objects.filter(
                username = usname,
                email = email,
                )
            if user !=0:
                return render(request, "core/auth/signup.html",{
                    "error" : "Такой пользователь уже существует"
                })
            print(user)
            User.objects.create_user(
                username = usname,
                email = email,
                password = password,
            )
            return redirect("signin")
        return render(request, "core/auth/signup.html", {
            "error" : "Проверьте поля для ввода данных"})
    return render(request, "core/auth/signup.html")


def signin(request):
    if request.method == "POST":
        password = request.POST.get("password")
        username = request.POST.get("username")
        user = authenticate(
            request, username=username, password=password
        )
        if user != None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "core/auth/signin.html", {
                "error" : "Неверный логин или пароль"
            })
    return render(request, "core/auth/signin.html")


def profile(request):
    return render(request, "core/auth/profile.html")


def signout(request):
    logout(request)
    return redirect("signin")