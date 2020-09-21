from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from testlesson.models import Book
from .models import UserAuthor, Article, Comment


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ['author']


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=False, label='Имя')
    last_name = forms.CharField(max_length=100, required=False, label='Фамилия')
    email = forms.EmailField(max_length=254)

    def save(self, *args, **kwargs):
        data = self.cleaned_data
        django_user = User.objects.create_user(
            username=data['username'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            password=data['password1'],
            email=data['email'],
            is_active=True
        )
        UserAuthor.objects.create(user=django_user)
        return django_user


class UserAuthorForm(forms.ModelForm):
    class Meta:
        model = UserAuthor
        exclude = ['user']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        exclude = ['author', 'count_view']

    def save(self, *args, **kwargs):

        if kwargs.get('author'):
            current_user = kwargs.pop('author')
            self.instance.author = current_user
        self.instance.save()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'article']
