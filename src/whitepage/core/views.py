from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from django.contrib.auth.decorators import login_required


@login_required(login_url='signin')
def index(request):
  return render(request, 'index.html')

def signup(request):
  if request.method == 'POST':
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    password2 = request.POST['password2']
    print(username)
    print(email)
    print(password)
    print(password2)
    
    if password == password2:
      if User.objects.filter(email=email).exists():
        messages.info(request, "Email Taken")
        return redirect('signup')
      elif User.objects.filter(username=username).exists():
        messages.info(request, "Username Taken")
        return redirect('signup')
      else:
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        
        #log user in and redirect to settings page
        
        #create profile for the new user
        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()
        return redirect('signup')
        
    else:
      messages.info(request, "Password Not Matching")
      return redirect('signup')
  else:
    return render(request, 'signup.html')
  
def signin(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)    
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
      auth.login(request, user)
      return redirect('/')
    
    else:
      messages.info(request, 'Credentials are invalid')
      return redirect('signin')
    

  else:  
    return render(request, 'signin.html')
  
def logout(request):
  auth.logout(request)
  return redirect('signin')

@login_required(login_url='signin')
def settings(request):
  return render(request, 'setting.html')