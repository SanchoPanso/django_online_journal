from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .forms import AnketaForm


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
