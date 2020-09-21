from django.shortcuts import render , redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate , login , logout

def login_(request):
    ctx = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        auth_user = authenticate(username=username, password= password)
        if auth_user:
            login(request, auth_user)
            return redirect('/')
        else:
            ctx['error'] = 'Invalid username or password'
    return render(request , 'users/auth/login.html', ctx)

def register_(request):
    ctx = {}
    ctx['form'] = SignUpForm
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_user = authenticate(username= user.username, password= form.cleaned_data['password1'])
            login(request, auth_user)
            return redirect('/')
            print('username' ,user.username)
            print('password' ,user.password)
        else:
            ctx['form'] = form
            print('**************invalid form!***********************')
    return render(request , 'users/auth/register.html', ctx)

def logout_(request):
    logout(request)
    return redirect('/')
