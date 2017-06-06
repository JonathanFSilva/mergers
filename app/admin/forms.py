# -*- coding: utf-8 -*-

from flask_wtf import FlaskForm 
from wtforms import StringField, DateField, FloatField, SubmitField
from wtforms.validators import DataRequired

class InvestimentoForm(FlaskForm):
    '''
    Formulário para o admin adicionar ou editar um investimento (a.k.a participação)
    '''
    tipo_invest = StringField('Tipo de investimento', validators=[DataRequired()])
    data_invest = StringField('Data e horário', validators=[DataRequired()], render_kw={"type": "date"})
    submit = SubmitField('Enviar')