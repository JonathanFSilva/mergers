# -*- coding: utf-8 -*-
# app/home/views.py

from flask import render_template
from flask_login import login_required

from . import home

@home.route('/')
@home.route('/index')
def homepage():
    """
    Exibe o HTML na rota / ou /index
    """
    return render_template('home/index.html', title='Bem Vindo!')

@home.route('/dashboard')
@login_required
def dashboard():
    """
    Exibe o HTML na rota /dashboard
    """
    return render_template('home/dashboard.html', title="Painel principal")
