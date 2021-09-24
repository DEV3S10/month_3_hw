from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from allauth.account.views import LoginView

# Create your views here.
from .models import BlogUser


def register_view(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            return HttpResponse("Passwords does not match!")

        user = BlogUser.objects.create_user(username=email, first_name=first_name,
                                            last_name=last_name, age=age, email=email, password=password)

        return HttpResponse("Registered successfully!")


def login_view(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('blogs')

        return render(request, 'login.html', context={"message": "Ne pravilnyi login ili parol"})


class MyLoginView(LoginView):
    template_name = 'login.html'


def logout_view(request):
    logout(request)
    return redirect('/users/login/')