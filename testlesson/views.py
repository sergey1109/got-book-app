from django.shortcuts import render
from django.http import HttpResponse
from . models import Book , Author

# Create your views here.
def home(request):
    all_books = Book.objects.all() 
    print('session', dict(request.session))
    return render (request  ,'testlesson/main_page.html',{
        'books' : all_books,
        'tab' : 'home'
    
    })
def about(request):
    ctx = {}
    ctx['tab'] ='about'
    return render(request, 'testlesson/about.html',ctx)

def book_detail(request, book_id):
    ctx = {}
    current_book = Book.objects.get(id=book_id)
    ctx['book'] = current_book
    return render(request ,'testlesson/book_detail.html',ctx)

def author_detail(request, author_id):
    current_author = Author.objects.get(pk=author_id)
    all_books = current_author.get_books()
    filter_books = [
      book for book in all_books if book.title.startswith('title')
    ]
    print('filter_books',filter_books)

    #all_books_by_author = current_author.get_books()
    ctx = {}
    ctx ['author'] = current_author
    #ctx ['books'] = all_books_by_author
    return render(request, 'testlesson/author_detail.html', ctx)