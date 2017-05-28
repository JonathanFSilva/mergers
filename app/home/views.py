# -*- coding: utf-8 -*-
# app/home/views.py

from flask import render_template, abort
from flask_login import login_required, current_user

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

# adiciona a view da dashboard do admin
@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    # previne o acesso do neguin não-admin
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title="Dashboard")