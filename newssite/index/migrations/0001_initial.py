# Generated by Django 4.2.6 on 2023-10-06 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('author', models.CharField(max_length=255, verbose_name='Автор')),
            ],
        ),
    ]