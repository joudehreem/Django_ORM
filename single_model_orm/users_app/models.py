from django.db import models
# Create your models here.


class User(models.Model):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField()
  age = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
        return f"User(id={self.id}, first_name={self.first_name}, last_name={self.last_name})"
      
  def create_user(first_name,last_name,email,age):
      User.objects.create(first_name=first_name,last_name=last_name,email=email,age=age)
    
  def get_data():
    return User.objects.all()
  
  def clear_user(id):
    remove=User.objects.get(id = id)
    remove.delete()

    
