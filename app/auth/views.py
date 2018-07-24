# -*- coding: utf-8 -*-
# app/auth/views.py

from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
from forms import LoginForm, RegistrationForm
from .. import db
from ..models import Empresa
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

@auth.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar():
    """
    Cuida da rota /cadastrar
    Adiciona uma empresa ao banco de dados
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        empresa = Empresa(email=form.email.data,
                            username=form.username.data,
                            razao_social=form.razao_social.data,
                            cnpj=form.cnpj.data,
                            password=form.password.data)

        # add employee to the database
        db.session.add(empresa)
        db.session.commit()
        flash('Cadastro feito com sucesso!')

        # redirect to the login page
        return redirect(url_for('auth.login'))

    # load registration template
    return render_template('auth/cadastrar.html', form=form, title='Cadastrar')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handle requests to the /login route
    Log an employee in through the login form
    """
    form = LoginForm()
    if form.validate_on_submit():

        # check whether employee exists in the database and whether
        # the password entered matches the password in the database
        empresa = Empresa.query.filter_by(email=form.email.data).first()
        if empresa is not None and empresa.verify_password(
                form.password.data):
            # log employee in
            login_user(empresa)

            # redireciona cada um para sua devida página
            if empresa.is_admin:
                return redirect(url_for('home.admin_dashboard'))

            else:
                return redirect(url_for('home.dashboard'))

        # when login details are incorrect
        else:
            flash('Email ou senha inválidos')

    # load login template
    return render_template('auth/login.html', form=form, title='Login')

@auth.route('/logout')
@login_required
def logout():
    """
    Handle requests to the /logout route
    Log an employee out through the logout link
    """
    logout_user()
    flash('Sessão encerrada com sucesso!')

    # redirect to the login page
    return redirect(url_for('auth.login'))
