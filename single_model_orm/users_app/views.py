from django.shortcuts import render,redirect
from .models import *
# from . import models
# Create your views here.

#To render the index.html & retrieve all data
def index(request):
  context={
      'users':User.get_data(),
  }
  return render(request, 'index.html',context)

#handle POST Request from users and  display the data to front-end
def add_user(request):
  if request.method == 'POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    age=request.POST['age']
    User.create_user(first_name,last_name,email,age)
    return redirect('/')
  
def delete_user(request,id):
    User.clear_user(id)
    return redirect('/')
  