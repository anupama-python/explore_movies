from django.contrib import auth, messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Malayalam, English, Hindi


# Create your views here.
def base(request):
    return render(request,"base.html")
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request)
            return redirect("movies")
        else:
            return redirect("movies")

    return render(request, 'login.html')


def register(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'register.html')





def movies(request):
    pass
    return render(request,"movies.html")

def malayalam(request):
    dict_mal={
        'mal':Malayalam.objects.all()
    }
    return render(request,"malayalam.html",dict_mal)
def english(request):
    dict_eng={
        'eng':English.objects.all()
    }
    return render(request,"english.html",dict_eng)
def hindi(request):
    dict_hin={
        'hin':Hindi.objects.all()
    }
    return render(request,"hindi.html",dict_hin)

def watch(request):
    return render(request,"watch.html")

def save(request):
    return render(request,"save.html")

def logout(request):
    return render(request,"logout.html")


