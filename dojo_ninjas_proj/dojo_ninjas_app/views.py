from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def index(request):
  
  context={
    'Dojos': all_dojo(),
  }
  return render(request,'index.html',context)

#Handel POST request in form Dojo
def form_dojo(request):
  if request.method=='POST':
    name=request.POST['name']
    city=request.POST['city']
    stat=request.POST['stat']
    create_dojo(name,city,stat)
    return redirect('/')

#Handel POST request in form Ninjas
def form_ninjas(request):
  if request.method=='POST':
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    dojo=request.POST['dojo']
    dojo_id=get_dojo_id(id=dojo)
    create_ninja(dojo_id,first_name,last_name)
    return redirect('/')
  
#Delete all dojos from database
def delete_dojos(request,id):
    if request.method == 'POST':
        delete_dojo (id)
    return redirect('/')