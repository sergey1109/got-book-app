from django.contrib import admin
from .models import Book, Author

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'is_sale','price', 'author']
    list_editable = [ 'title', 'is_sale','price', 'author']
    list_filter = ['genre']

admin.site.register(Book,BookAdmin)
admin.site.register(Author)