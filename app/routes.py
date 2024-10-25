import os
from pathlib import Path

from flask import render_template, get_template_attribute, redirect, url_for, flash
from starlette.templating import Jinja2Templates
from app.forms import LoginForm
from app import app


@app.route("/")
@app.route("/index")
def index():
    # Получаем путь к директории шаблонов из конфигурации Flask
    # template_folder = app.template_folder
    #
    # print(f"Путь к директории шаблонов: {template_folder}")
    #
    # # Проверяем существование директории шаблонов
    # if not os.path.exists(template_folder):
    #     raise FileNotFoundError("Директория шаблонов не найдена.")

    # Создаем список всех файлов в директории шаблонов
    # templates = [f for f in os.listdir(template_folder) if f.endswith('.html')]
    #
    # print(f"Найдены следующие шаблоны: {templates}")
    #
    # # Проверяем наличие файла index.html
    # if 'index.html' not in templates:
    #     raise FileNotFoundError("Файл index.html не найден в директории шаблонов.")

    user = {'username': 'Константин'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Запрашиваемый логин для пользователя {}, Запомнить {}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Войти в систему', form=form)
