# Generated by Django 3.0.8 on 2020-09-10 14:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок статьи')),
                ('lead', models.CharField(max_length=500, verbose_name='Краткое описание')),
                ('content', models.TextField(max_length=15000, verbose_name='Контент статьи')),
                ('count_view', models.IntegerField(default=0)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.UserAuthor')),
            ],
        ),
    ]
