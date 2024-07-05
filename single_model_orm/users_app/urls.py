from django.urls import path
from . import views

urlpatterns= [
  path('',views.index),
  path('add_user',views.add_user),
  path('delete_user/<int:id>', views.delete_user, name='delete_user'),
]