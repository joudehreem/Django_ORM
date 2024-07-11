from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('form_dojo',views.form_dojo),
    path('form_ninjas',views.form_ninjas),
    path('delete_dojos/<int:id>', views.delete_dojos),
]