

from django.db import models

# Create your models here.

class Book(models.Model):
  title = models.CharField(max_length=225)
  desc = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def __str__(self):
    return f'{self.title}'
  
class Author(models.Model):
  first_name = models.CharField(max_length=225)
  last_name = models.CharField(max_length=225)
  notes =  models.TextField()
  books = models.ManyToManyField(Book,related_name="authors")
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  def __str__(self):
    return f'{self.first_name}'
  
#Get all books
def all_books():
  return Book.objects.all()
#create a new book using request post
def create_books(request):
  Book.objects.create(title = request.POST['title'],  
                      desc = request.POST['desc'])
#Get a book by ID
def get_book(id_book):
    return Book.objects.get(id=id_book)

#Get all authors
def all_authors():
  return Author.objects.all()

#create a new author using request post
def create_authors(request):
  Author.objects.create(
          first_name = request.POST['first_name'],
          last_name = request.POST['last_name'])
  
#Get an author by ID
def get_author(id_author):
    return Author.objects.get(id=id_author)


