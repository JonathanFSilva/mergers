# -*- coding: utf-8 -*-

# app/admin/forms.py

from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, FloatField, SubmitField, SelectField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField

from ..models import Empresa

class InvestimentoForm(FlaskForm):
    '''
    Formulário para o admin adicionar ou editar um investimento (a.k.a participação)
    '''
    tipo_invest = SelectField('Tipo de investimento', 
                    choices=[('Participação Societária', 'Participação Societária'), 
                             ('Investimento em Sociedade anônima', 'Investimento em Sociedade anônima')])
    data_invest = StringField('Data e horário', validators=[DataRequired()], render_kw={"type": "date"})
    empresa_investidora = QuerySelectField(query_factory=lambda: Empresa.query.filter_by(is_admin=False),
                                    get_label='razao_social')
    # SELECT razao_social FROM empresa WHERE is_admin = 0
    empresa_investida = QuerySelectField(query_factory=lambda: Empresa.query.filter_by(is_admin=False),
                                    get_label='razao_social')
    submit = SubmitField('Enviar')
    