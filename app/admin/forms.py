# -*- coding: utf-8 -*-

# app/admin/forms.py

from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Empresa
import time
from datetime import date, datetime, time

# pega a data de hoje
hoje = date.today()

class InvestimentoForm(FlaskForm):
    '''
    Formulário para o admin adicionar ou editar um investimento (a.k.a participação)
    '''
    tipo_invest = SelectField('Tipo de investimento', 
                    choices=[('Participação Societária', 'Participação Societária'), 
                             ('Investimento em Sociedade anônima', 'Investimento em Sociedade anônima')
                            ])
    data_invest = StringField('Data e horário',
                             validators=[DataRequired()], 
                             default=hoje, 
                             render_kw={"type": "date"}
                             )
    empresa_pai = QuerySelectField(query_factory=lambda: Empresa.query.filter_by(is_admin=0),
                                    get_label='razao_social')
                                    
    # SELECT razao_social FROM empresa WHERE is_admin = 0
    empresa_filha = QuerySelectField(query_factory=lambda: Empresa.query.filter_by(is_admin=0),
                                    get_label='razao_social')
    submit = SubmitField('Enviar')
    