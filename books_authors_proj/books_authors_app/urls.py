

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_book),
    path('register_book_form', views.register_book_form),
    path('books/<int:id_book>',views.view_book),
    path('authors_add_book/<int:id_book>', views.authors_add_book),



    path('authors/', views.index_author),
    path('register_author_form', views.register_author_form,),
    path('authors/<int:id_author>', views.view_author),
    path('books_add_author/<int:id_author>', views.books_add_author),
]
