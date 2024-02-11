from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def SignupPage(request):
    if request.method == 'POST' or request.method == 'post':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            return HttpResponse('Invalid password! Password did not match!')
        else:
            myuser = User.objects.create_user(username, email, password1)
            myuser.save()
            print(myuser)
            return redirect('auth_system:login')
        
        print(username, email, password1, password2)
        
    return render(request, 'auth_system/signup.html')


def LoginPage(request):
    if request.method == 'POST' or request.method == 'post':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('task:index')
        else:
            return HttpResponse('Invalid Credentials!')
        
    return render(request, 'auth_system/login.html')

def LogoutPage(request):
    logout(request)
    return redirect('task:index')