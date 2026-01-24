import datetime
import os

from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request) -> HttpResponse:
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request) -> HttpResponse:
    # обратите внимание – здесь HTML шаблона нет, 
    # возвращается просто текст
    current_time = datetime.datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request) -> HttpResponse:
    # по аналогии с `time_view`, напишите код,
    # который возвращает список файлов в рабочей 
    # директории
    current_dir = os.getcwd()

    files = []
    for item in os.listdir(current_dir):
        if os.path.isfile(os.path.join(current_dir, item)):
            item = f'📄 {item}<br/>'
            files.append(item)
        else:
            item = f'📁 {item}<br/>'
            files.append(item)

    return HttpResponse(files)
