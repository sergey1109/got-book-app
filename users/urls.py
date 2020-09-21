from django.urls import path ,include
from .views import user_page, cabinet,\
    write_post, my_articles,\
    delete_article, update_article,\
    add_to_session, bucket,\
    delete_bucket,articles,\
    article_detail, add_comment,\
    js_examples
from .auth_views import login_ , register_, logout_

app_name = 'client_app'

urlpatterns = [
    path('',user_page, name='index'),
    path('cabinet',cabinet, name='profile'),
    path('write_post',write_post, name='write_post'),
    path('my_articles',my_articles, name='my_articles'),
    path('delete_article<int:pk>',delete_article, name='delete_article'),
    path('update_article<int:pk>',update_article, name='update_article'),
    path('add_to_session<int:pk>',add_to_session, name='add_to_session'),
    path('bucket',bucket, name='bucket'),
    path('delete_bucket<int:pk>',delete_bucket, name='delete_bucket'),
    path('article_detail<int:pk>',article_detail, name='article_detail'),
    path('add_comment<int:id_article>',add_comment, name='add_comment'),
    path('articles',articles, name='articles'),
    path('js_examples',js_examples, name='js_examples'),


]
auth_urls = [
    path('login_user',login_, name='login'),
    path('register',register_, name='register'),
    path('logout',logout_, name='logout'),
]

urlpatterns += auth_urls

