
from django.urls import path
from .views import (home as H, about, book_detail, author_detail)

urlpatterns = [
    path('', H),
    path('about/', about),
    path('book-detail/<int:book_id>/' , book_detail),
    path('author-detail/<int:author_id>/' , author_detail),

]
