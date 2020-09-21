from django.shortcuts import render, redirect, HttpResponse

from .forms import BookForm, UserAuthorForm, ArticleForm,CommentForm 
from .models import UserAuthor, Article, Comment
from testlesson.models import Book


# Create your views here.

def user_page(request):
    ctx = {}
    ctx['form'] = BookForm
    if request.method == 'GET':
        return render(request, 'users/index.html', ctx)
    elif request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            ctx['success'] = True
        return render(request, 'users/index.html', ctx)


def cabinet(request):
    ctx = {}
    ctx ['cabinet_tab'] = 'profile'
    if request.method == 'GET':
        try :
            user_author = UserAuthor.objects.get(user=request.user.id)
            ctx ['form'] = UserAuthorForm(instance=user_author)
        except Exception as e:
            ctx ['form'] = UserAuthorForm
    if request.method == 'POST':
        form = UserAuthorForm(request.POST)
        if form.is_valid():
            user_author = UserAuthor.objects.get(user=request.user.id)
            user_author.bio = form.cleaned_data['bio']
            user_author.type_view = form.cleaned_data['type_view']
            user_author.pseudoname = form.cleaned_data['pseudoname']
            user_author.save()
            ctx['form'] = UserAuthorForm(instance=user_author)
            ctx['saved'] = True
            print('user_author' , user_author)
        else:
            print('is not valid !')
    return render(request, 'users/cabinet/profile.html', ctx)


def write_post(request):
    ctx = {}
    ctx ['cabinet_tab'] = 'write_post'
    ctx ['form'] = ArticleForm
    user = UserAuthor.objects.get(user=request.user.id)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save(author=user)
            ctx['saved'] = True
    return render(request, 'users/cabinet/write_post.html', ctx)

def my_articles(request):
    ctx = {}
    all_articles = Article.objects.filter(author__user_id=request.user.id)
    ctx ['articles'] = all_articles
    ctx['cabinet_tab'] = 'my_articles'
    print (all_articles , 'all_articles ')
    return render(request , 'users/cabinet/my_articles.html', ctx)

def delete_article(request, pk):
    article = Article.objects.get(id=pk)
    article.delete()
    return redirect('client_app:my_articles')


def update_article(request, pk):
    ctx = {}
    article = Article.objects.get(pk=pk, author__user_id=request.user.id)
    form = ArticleForm(instance=article)
    ctx['form']= form
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('client_app:my_articles')
        else:
            ctx['form'] = form 
            print ('invalid form')
    return render(request, 'users/cabinet/write_post.html', ctx)


def add_to_session(request, pk):
    ctx = {}
    aritcles_in_session = request.session.get('books_bucket', [])
    print ('before append')
    if pk not in aritcles_in_session:
        aritcles_in_session.append(pk)
    request.session['books_bucket'] = aritcles_in_session
    print('after append ')
    
    return redirect('/')


def bucket(request):
    ctx = {}
    books_ids = request.session.get('books_bucket', [])
    if books_ids:
        all_books = [Book.objects.get(pk=books_id) for books_id in books_ids]
        total_price = 0
        for book in all_books:
            if book.is_sale and book.new_price:
                total_price += book.new_price 
            else:
                total_price += book.price
        ctx['books'] = all_books
        ctx['total_price'] = total_price
        print(all_books)
        print('books_ids', books_ids)
    return render(request, 'users/bucket.html',ctx)


def delete_bucket(request, pk):
    books_ids = request.session.get('books_bucket', [])
    if pk in books_ids:
        books_ids.remove(pk)
        request.session['books_bucket'] = books_ids
        return redirect('client_app:bucket')
        
def articles(request):
    ctx = {}
    all_articles = Article.objects.all().order_by('-id')
    ctx['articles'] = all_articles
    return render(request, 'users/all_articles.html',ctx)

def article_detail(request,pk):
    ctx ={}
    ctx ['article'] = Article.objects.get(pk=pk)
    ctx['form'] = CommentForm 
    return  render(request , 'users/article.html', ctx)


def add_comment(request,id_article):
    article = Article.objects.get(pk=id_article)
    comment_author = UserAuthor.objects.get(user_id=request.user.id)
    form = CommentForm(request.POST)
    if form.is_valid():
        text = form.cleaned_data['text']
        props = {
            'user': comment_author,
            'article': article,
            'text': text,
        }
        Comment.objects.create(**props)
        print ('article', article )
        print ('comment_author', comment_author )
        print ('text', text)
   # print('add_comment', id_article)
    return redirect('client_app:article_detail', pk=id_article)

def js_examples(request):
    ctx = {}
    return render(request,'users/examples_js.html',ctx)