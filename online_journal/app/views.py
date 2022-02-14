from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from .forms import AnketaForm, CommentForm
from .models import Comment, Blog


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Домашняя страница',
            'year': datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title': 'Контакты',
            'message': 'Сведения о наших контактах',
            'year': datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title': 'О нас',
            'message': 'Сведения о нас',
            'year': datetime.now().year,
        }
    )


def anketa(request):
    assert isinstance(request, HttpRequest)
    data = None
    gender = {'1': 'Мужской',
              '2': 'Женский'}
    internet = {'1': 'Каждый день',
                '2': 'Несколько раз в день',
                '3': 'Несколько раз в неделю',
                '4': 'Несколько раз в месяц'}

    if request.method == 'POST':
        form = AnketaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['city'] = form.cleaned_data['city']
            data['job'] = form.cleaned_data['job']
            data['gender'] = gender[form.cleaned_data['gender']]
            data['internet'] = internet[form.cleaned_data['internet']]
            if form.cleaned_data['notice'] is True:
                data['notice'] = "Да"
            else:
                data['notice'] = "Нет"
            data['email'] = form.cleaned_data['email']
            data['message'] = form.cleaned_data['message']
            form = None
    else:
        form = AnketaForm()
    return render(
        request,
        'app/anketa.html',
        {
            'form': form,
            'data': data
        }
    )


def registration(request):
    """
    Renders the registration page.
    """

    assert isinstance(request, HttpRequest)
    if request.method == "POST":    # после отправки формы
        regform = UserCreationForm (request.POST)

        if regform.is_valid():  # валидация полей формы

            reg_f = regform.save(commit=False)  # не сохраняем автоматически данные формы
            reg_f.is_staff = False      # запрещен вход в административный раздел
            reg_f.is_active = True      # активный пользователь
            reg_f.is_superuser = False  # не является суперпользователем
            reg_f.date_joined = datetime.now()  # дата регистрации
            reg_f.last_login = datetime.now()   # дата последней авторизации
            reg_f.save()    # сохраняем изменения после добавления данных
            return redirect('home')     # переадресация на главную страницу после регистрации

    else:

        regform = UserCreationForm()    # создание объекта формы для ввода данных нового пользователя
        return render(
            request,
            'app/registration.html',
            {
                'regform': regform,     # передача формы в шаблон веб-страницы
                'year': datetime.now().year,
                }
            )


def blog(request,):
    """Renders the blog page."""
    posts = Blog.objects.all()
    # и запрос на выбор всех статей из модели
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title': 'Блог',
            'posts': posts,
            'year': datetime.now().year,
        }
    )


def blogpost(request, parameter):
    """Renders the blogpost page"""
    post_1 = Blog.objects.get(id=parameter)
    # comments = Comment.objects.filter(post=parameter)

    ###
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1,
            'year': datetime.now().year,
        }
    )
