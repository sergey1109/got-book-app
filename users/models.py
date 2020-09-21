from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserAuthor(models.Model):
    TYPE_USER_VIEW = (
        ('fio', 'ФИО'),
        ('pseudo_name', 'Псевдоним'),
    )
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    bio = models.TextField(max_length=5000)
    type_view = models.CharField(choices=TYPE_USER_VIEW,
                                 max_length=len('pseudo_name'),
                                 verbose_name='Тип представления',
                                 blank=True, null=True)
    pseudoname = models.CharField(max_length=150,
                                  verbose_name='Псевдоним ',
                                  blank=True, null=True)
    def get_type_view(self):
        if self.type_view == 'fio':
            return f'{self.user.first_name}{self.user.last_name}'
        elif self.type_view == 'pseudo_name':
            return self.pseudoname
        else:
            return self.user.username

    def __str__(self):
        return self.user.username

class Article(models.Model):
    author = models.ForeignKey(UserAuthor , on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, verbose_name= 'Заголовок статьи')
    lead = models.CharField(max_length=500, verbose_name='Краткое описание')
    content = models.TextField(max_length=15000,verbose_name='Контент статьи')
    count_view = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}{self.author.user.username}'
    
    
    def get_comments(self):
        return Comment.objects.filter(article=self)

class Comment(models.Model):
    user = models.ForeignKey(UserAuthor, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField(max_length=500,blank=True,null=True)
    date = models.DateTimeField(auto_now_add=True)
    __str__ = lambda self: self.text
    
    