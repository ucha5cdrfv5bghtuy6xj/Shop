from django.shortcuts import render

# Create your views here.
def signup(request):
    return render(request, "core/auth/signup.html")


def signin(request):
    return render(request, "core/auth/signin.html")


def profile(request):
    return render(request, "core/auth/profile.html")


def signout(request):
    pass