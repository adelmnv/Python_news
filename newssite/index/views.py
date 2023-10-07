from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from .models import *

# Create your views here.
menu = [
    {'title' : 'Главная', 'url_name' : 'home'},
    {'title' : 'Новости','url_name' : 'home'},
]
def main(request):
    news = News.objects.all()
    my_context = {
        'title': 'Новости',
        'menu': menu,
        'news': news
    }
    return render(request, 'index/index.html', context=my_context)

def pageNotFound(request, exception):
    return HttpResponseNotFound(f'<h1>Page not found</h1>')