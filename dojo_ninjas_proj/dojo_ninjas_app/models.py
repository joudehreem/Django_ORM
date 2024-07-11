from django.db import models

# Create your models here.

class Dojo(models.Model):
  name = models.CharField(max_length=255)
  city = models.CharField(max_length=255)
  stat = models.CharField(max_length=2)
  desc = models.CharField(max_length=10,default='old dojo')

class Ninja(models.Model):
  dojo = models.ForeignKey(Dojo, related_name='ninjas',on_delete=models.CASCADE)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  
  #Get All the data from Dojo Class
def all_dojo():
  return Dojo.objects.all()

  #Use function Create Dojo to recall inside form_dojo
def create_dojo(name,city,stat):
  Dojo.objects.create(name=name,city=city,stat=stat)
  
  #Use function Create Ninjas to recall inside form_ninja
def create_ninja(dojo,first_name,last_name):
    Ninja.objects.create(dojo=dojo, first_name=first_name,last_name=last_name)

#Use function to recall id inside form_ninja

def get_dojo_id(id):
    return Dojo.objects.get(id=id)
  

#Delete all dojos from database
def delete_dojo (id):
  dojo = Dojo.objects.get(id=id)
  dojo.delete()