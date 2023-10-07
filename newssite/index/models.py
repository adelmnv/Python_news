from django.db import models
from django.urls import reverse

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.CharField(max_length=255, verbose_name='Автор')
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-date']

