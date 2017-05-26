# -*- coding: utf-8 -*-
# app/models.py

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class Empresa(UserMixin, db.Model):
    """
    cria a tabela Empresa 
    """

    # Garante que o nome da tabela estará no plural
    # assim como no modelo
    __tablename__ = 'empresas'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    razao_social = db.Column(db.String(60), index=True, unique=True)
    cnpj = db.Column(db.String(18), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean, default=False)
    investimento_id = db.Column(db.Integer, db.ForeignKey('investimentos.id'))


    @property
    def password(self):
        """
        previne acesso indesejado à senha 
        """
        raise AttributeError('A senha não é um atributo legível.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<Empresa: {}>'.format(self.razao_social)

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return Empresa.query.get(int(user_id))

class Investimento(db.Model):
    """
    Create a Department table
    """

    __tablename__ = 'investimentos'

    id = db.Column(db.Integer, primary_key=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresas.id'))
    tipo_invest = db.Column(db.String(60), unique=True)
    val_invest = db.Column(db.Float(7))
    data_invest = db.Column(db.DateTime)
    investimento = db.relationship('Empresa', backref='investimento', lazy='dynamic')

    def __repr__(self):
        return '<Investimento: {}>'.format(self.tipo_invest)
