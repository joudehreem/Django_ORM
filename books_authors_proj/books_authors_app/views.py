from django.shortcuts import render,redirect
from .models import *
# Create your views here.


#show all books and render the books page
def index_book(request):
  context={
    'books':all_books(),
  }
  return render(request,'books.html',context)

# Form to enter new book And handle the post request
def register_book_form(request):
  if request.method == 'POST':
    create_books(request)
    return redirect('/')
  
# view the details of book
def view_book(request,id_book):
  context={
    'book':get_book(id_book),
    'authors': Author.objects.exclude(books = id_book)
  }
  return render(request,'book_view.html',context)

def authors_add_book(request,id_book):
    this_book =  get_book(id_book)
    author = get_author(request.POST['id_author'])
    this_book.authors.add(author)
    return redirect(f'/books/{id_book}')


#show all authors and render the authors page
def index_author(request):
  context={
  'authors':all_authors(),
  }
  return render(request,'authors.html',context)

# Form to enter new author And handle the post request
def register_author_form(request):
  if request.method == 'POST':
    create_authors(request)
    return redirect('/authors')
  
# view the details of book
def view_author(request,id_author):
    context={
      'author': get_author(id_author),
      'books' : Book.objects.exclude(authors = id_author),
    }
    return render(request,'author_view.html',context)
  
def books_add_author(request, id_author):
    this_author = get_author(id_author)
    if request.method == "POST":
      book = get_book(request.POST['id_book'])
      this_author.books.add(book)
      return redirect(f'/authors/{id_author}')   





#SET NUL, CASCASED, PROTECTED

