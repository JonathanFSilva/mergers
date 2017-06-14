# -*- coding: utf-8 -*-

# app/admin/views.py

from flask import abort, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import admin
from forms import InvestimentoForm
from .. import db
from ..models import Investimento
from ..models import Empresa

def check_admin():
    """
    Previne usuário comum de acessar certas páginas
    """
    if not current_user.is_admin:
        abort(403)
        
@admin.route('/investimentos', methods=['GET', 'POST'])
@login_required
def listar_invest():
    """
    lista todos os investimentos
    """
    
    check_admin()
    
    investimentos = Investimento.query.all()
    
    return render_template('admin/investimentos/investimentos.html',
                            investimentos=investimentos, title="Investimentos")

@admin.route('/investimentos/incluir', methods=['GET', 'POST'])
@login_required
def incluir_invest():
    """
    adiciona um investimento ao banco de dados
    """
    
    check_admin()
    
    # esta mesma variável será utilizada nos templates!
    add_invest = True 
    
    form = InvestimentoForm()
    if form.validate_on_submit():
        # corta apenas o nome da empresa pai
        pai = form.empresa_pai.data
        pai = str(pai)
        pai = pai[9:len(pai) - 1]
        
        # corta apenas o nome da empresa filha
        filha = form.empresa_filha.data
        filha = str(filha)
        filha = filha[9:len(filha) - 1]
        
        if pai == filha:
            flash('Erro: Uma empresa não pode investir em si mesma!')
            # não inclui investimento e retorna
            return redirect(url_for('admin.listar_invest'))
        
        investimento = Investimento(tipo_invest=form.tipo_invest.data,
                                    data_invest=form.data_invest.data,
                                    empresa_pai=pai,
                                    empresa_filha=filha
                                    )

        try:
            # adiciona investimento ao banco de dados
            db.session.add(investimento)
            db.session.commit()
            flash('Investimento incluído com sucesso!')
            
        except:
            # caso o nome do investimento já exista
            flash('Erro: Este investimento já existe!')
            
        # redireciona usuário para a página de investimentos
        return redirect(url_for('admin.listar_invest'))
        
    # carrega o template do investimento
    return render_template('/admin/investimentos/investimento.html', action="Incluir",
                            add_invest=add_invest, form=form, title="Incluir investimento")
    
@admin.route('/investimentos/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_invest(id):
    """
    Edita um investimento
    """
    check_admin()
    
    add_invest = False
    
    investimento = Investimento.query.get_or_404(id)
    form = InvestimentoForm(obj=investimento)
    if form.validate_on_submit():

        # corta apenas o nome da empresa pai
        pai = form.empresa_pai.data
        pai = str(pai)
        pai = pai[9:len(pai) - 1]
        
        # corta apenas o nome da empresa filha
        filha = form.empresa_filha.data
        filha = str(filha)
        filha = filha[9:len(filha) - 1]
        
        if pai == filha:
            flash('Erro: Uma empresa não pode investir em si mesma!')
            # não inclui investimento e retorna
            return redirect(url_for('admin.listar_invest'))
        
        investimento.tipo_invest = form.tipo_invest.data
        investimento.data_invest = form.data_invest.data
        investimento.empresa_filha = filha
        investimento.empresa_pai = pai
        db.session.commit()
        flash('Investimento editado com sucesso!')
        
        # redireciona para a página de investimentos
        return redirect(url_for('admin.listar_invest'))
        
    form.tipo_invest.data = investimento.tipo_invest
    return render_template('/admin/investimentos/investimento.html', action="Editar",
                            add_invest=add_invest, form=form, investimento=investimento,
                            title="Editar investimento")
                            
@admin.route('/investimentos/deletar/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_invest(id):
    """
    deleta um investimento do banco de dados
    """
    check_admin()
    
    investimento = Investimento.query.get_or_404(id)
    db.session.delete(investimento)
    db.session.commit()
    flash('Investimento deletado com sucesso!')
    
    # redireciona para a página dos investimentos
    return redirect(url_for('admin.listar_invest'))
    
@admin.route('/empresas')
@login_required
def listar_empresas():
    """
    Lista todas as empresas
    """
    
    check_admin()
    
    empresas = Empresa.query.all()
    
    return render_template('admin/empresas/empresas.html',
                            empresas=empresas, title='Empresas')
                            
@admin.route('/arvore')
@login_required
def arvores():
    """
    Mostra a árvore societária de todas as empresas cadastradas
    no app
    """
    
    check_admin()
    
    investimentos = Investimento.query.all()
    
    return render_template('admin/arvores/arvores.html',
                            investimentos=investimentos, title='Árvore')