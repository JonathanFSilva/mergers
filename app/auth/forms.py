# -*- coding: utf-8 -*-
# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Empresa

class RegistrationForm(FlaskForm):
    """
    Formulário para usuários criarem novas contas
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Usuário', validators=[DataRequired()])
    razao_social = StringField('Empresa', validators=[DataRequired()])
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[
                                        DataRequired(),
                                        EqualTo('confirm_password')
                                        ])
    confirm_password = PasswordField('Confirme a senha')
    submit = SubmitField('Cadastrar')

    def validate_email(self, field):
        if Empresa.query.filter_by(email=field.data).first():
            raise ValidationError('Este email já está em uso!')

    def validate_username(self, field):
        if Empresa.query.filter_by(username=field.data).first():
            raise ValidationError('Este nome de usuário já está em uso!')

class LoginForm(FlaskForm):
    """
    Formulário para login de usuários
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Senha', validators=[DataRequired()])
    submit = SubmitField('Login')
