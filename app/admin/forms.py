from flask_wtf import FlaskForm 
from wtforms import StringField, DateTimeField, FloatField, SubmitField
from wtforms.validators import DataRequired

class InvestimentoForm(FlaskForm):
    """
    Formulário para o admin adicionar ou editar um investimento (a.k.a participação)
    """
    tipo_invest = StringField('Tipo de investimento', validators=[DataRequired()])
    val_invest = FloatField('Valor do investimento', validators=[DataRequired()])
    data_invest = DateTimeField('Data e horário', format='%d-%m-%Y %H:M')
    submit = SubmitField('Enviar')