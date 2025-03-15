from django.shortcuts import render
from .models import Book

# Create your views here.

# books = [
#   {
#     'id': 1, 'name': 'Django for Beginners', 'author': 'William S. Vincent', 'published': '2024-07-10', 'pages': 357, 'price': 48, 'description': 'Django for Beginners, 5th Edition: Build Modern Web Applications with Python'
#   },
#   {
#     'id': 2, 'name': 'Django 5 By Example', 'author': 'Antonio Melé', 'published': '2024-04-30', 'pages': 820, 'price': 30, 'description': 'Django 5 By Example: Build powerful and reliable Python web applications from scratch'
#   },
#   {
#     'id': 3, 'name': 'Django in Action', 'author': 'Christopher Trudeau', 'published': '2024-08-06', 'pages': 400, 'price': 37, 'description': 'Build professional quality web applications using Python and the Django 5.0 web framework.'
#   },
#   {
#     'id': 4, 'name': 'Django for APIs', 'author': 'William S. Vincent', 'published': '2025-03-04', 'pages': 216, 'price': 38, 'description': 'Django for APIs, 5th Edition: Build Web APIs with Python and Django',
#   },
# ]
def index(request):
  search_term = request.GET.get('searchstring')
  if search_term:
    books = Book.objects.filter(name__icontains=search_term)
  else:
    books = Book.objects.all()
  template_data = {}
  template_data['title'] = 'Books'
  template_data['books'] = books
  # template_data['books'] = Book.objects.all()
  return render(request, 'books/index.html', 
                {'template_data': template_data})

def show(request, id):
  book = Book.objects.get(id=id)
  # book = books[id - 1]
  template_data = {}
  template_data['title'] = book.name
  # template_data['title'] = book['name']
  template_data['book'] = book
  return render(request, 'books/show.html', 
                {'template_data': template_data})
