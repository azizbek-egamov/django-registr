from django.shortcuts import render, redirect
from django.http import *
from .models import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User


people = [
    {
        "ism": "Akmal",
        "familiya": "Karimov",
        "yoshi": 28,
        "jinsi": "Erkak",
        "telefon": "+998901234567",
    },
    {
        "ism": "Dilnoza",
        "familiya": "Tursunova",
        "yoshi": 24,
        "jinsi": "Ayol",
        "telefon": "+998901234568",
    },
    {
        "ism": "Sardor",
        "familiya": "Rasulov",
        "yoshi": 30,
        "jinsi": "Erkak",
        "telefon": "+998901234569",
    },
    {
        "ism": "Feruza",
        "familiya": "Ismoilova",
        "yoshi": 26,
        "jinsi": "Ayol",
        "telefon": "+998901234570",
    },
    {
        "ism": "Jasur",
        "familiya": "Norboev",
        "yoshi": 32,
        "jinsi": "Erkak",
        "telefon": "+998901234571",
    },
]


def homePage(request):
    u = request.user
    print(u)
    if str(u) == "AnonymousUser":
        return render(request, "index.html", {"user": 'Nomalum foydalanuvchi'})
    elif str(u) == "admin":
        return redirect("/admin")
    else:
        return render(request, "index.html", {"user": u})


def aboutPage(request):
    return render(request, "about.html", {"book": Book.objects.all()})


def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(
                request,
                "login.html",
                {
                    "error": "Login yoki parol noto'g'ri",
                    "clas": "error",
                    "us": username,
                    "ps": password,
                },
            )

    return render(request, "login.html")


def LogoutPage(request):
    logout(request)
    return redirect("home")


def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        email = request.POST.get("email")
        if pass1 == pass2:
            print(User.objects.filter(username=username).exists())
            if User.objects.filter(username=username).exists():
                return render(
                    request,
                    "signup.html",
                    {
                        "error": "Ushbu user band, boshqa o'ylab toping",
                        "clas": "error",
                        "em": email,
                        "us": username,
                        "p1": pass1,
                        "p2": pass2,
                    },
                )
            elif User.objects.filter(email=email).exists():
                return render(
                    request,
                    "signup.html",
                    {
                        "error": "Ushbu email band, boshqa email kiriting",
                        "clas": "error",
                        "em": email,
                        "us": username,
                        "p1": pass1,
                        "p2": pass2,
                    },
                )
            else:
                user = User.objects.create_user(
                    username=username, email=email, password=pass1
                )
                user.save()
                login(request, user)
                return redirect("home")
        else:
            return render(
                request,
                "signup.html",
                {
                    "error": "Parollar mos kelmayabdi",
                    "clas": "error",
                    "em": email,
                    "us": username,
                    "p1": pass1,
                    "p2": pass2,
                },
            )
    return render(request, "signup.html")


def contactPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        lname = request.POST.get("lname")
        age = request.POST.get("age")
        # print(name, lname, age)
        Users.objects.create(name=name, fname=lname, age=age)
        return redirect("about")
    else:
        return render(request, "contact.html")


def UpdatePage(request, id):
    try:
        user = Users.objects.get(id=id)
        if request.method == "POST":
            user.name = request.POST.get("name")
            user.fname = request.POST.get("lname")
            user.age = request.POST.get("age")
            Users.save()
            return redirect("about")

        return render(request, "update.html", {"cls": Users.objects.get(id=id)})
    except:
        return redirect("about")


def DeletePage(request, id):
    try:
        user = Users.objects.get(id=id)
        user.delete()
        return redirect("about")
    except:
        return redirect("about")


# Create your views here.
