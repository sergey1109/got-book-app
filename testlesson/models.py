from django.db import models

# Create your models here.
class Author (models.Model):
    name = models.CharField(max_length=35,verbose_name='Имя автора')
    surname = models.CharField(max_length=35,verbose_name='Фамилия ')
    date_birth = models.DateField(verbose_name='Дата рождения')
    date_dead = models.DateField(verbose_name='Дата смерти',blank=True,null=True)
    bio = models.TextField(max_length=5000,verbose_name='Био автора')

    def __str__(self):
        return f'{self.name} - {self.surname}'

    def front_name(self):
        return f'{self.name.capitalize()} {self.surname.capitalize()}'

    def get_books(self):
        return Book.objects.filter(author_id=self.id)

    def get_total_price(self):
        books = self.get_books()
        price_list = []
        for book in books:
            if book.is_sale:
                price_list.append(book.new_price or 0)
            else:
                price_list.append(book.price or 0)
        return  sum(price_list)


    def count_sale(self):
        return len(self.get_books().filter(is_sale=True))


    def count_is_not_sale(self):
        return len(self.get_books().filter(is_sale=False))


class Book(models.Model):
    GENRE_CHOISE = (
        ('comedy', 'Комедия'),
        ('trag', 'Боевик'),
        ('melodrama', 'Драма'),
        ('futur', 'Фанатаска'),
    )
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='', null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    is_sale = models.BooleanField(default=False)
    new_price = models.FloatField(blank=True,null=True)
    genre = models.CharField(choices=GENRE_CHOISE,max_length=100)


    def __str__(self):
        return f'title - {self.title}'




