from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.contrib import messages
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User

# Create your views here.


def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"Username does not exist",extra_tags='error')   

        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            messages.success(request,"User successfully logged in",extra_tags='success')
            # get the previous page URL from the session
            previous_page_url = request.session.get('previous_page_url', '/')
            # redirect to the previous page
            return redirect(previous_page_url)

        else:
            messages.error(request,"Username or password is incorrect",extra_tags='error')    
    
    # store the current page URL in the session
    request.session['previous_page_url'] = request.META.get('HTTP_REFERER', '/')
    return render(request,'members/login.html')

def logoutUser(request):
    logout(request)
    messages.success(request,"User succesfully logged out",extra_tags='success')
    return render(request, 'members/login.html')

def registerUser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            
            messages.success(request,"User Account was created",extra_tags='success')
            
            login(request,user)
            return redirect('home')   
    else:
        form = SignUpForm()
    return render(request, 'members/register.html', {'form': form})