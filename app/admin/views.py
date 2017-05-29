# -*- coding: utf-8 -*-

# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import InvestimentoForm
from .. import db
from ..models import Investimento

def check_admin():
    """
    Previne usuário comum de acessar certas páginas
    """
    if not current_user.is_admin:
        abort(403)
        
@admin.route('/investimentos', methods=['GET', 'POST'])
@login_required
def listar_investimentos():
    """
    lista todos os investimentos
    """
    
    check_admin()
    
    investimentos = Investimento.query.all()
    
    return render_template('admin/investimentos/investimentos.html',
                            investimentos=investimentos, title="Investimentos")
