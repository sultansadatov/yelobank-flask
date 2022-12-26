from logging import PlaceHolder
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField,FileField
from wtforms.validators import DataRequired, Length
choices1=['Prefix','050', '051', '055','070', '077', '090','010']
choices2=['Filialı seç', 'Baş ofis / MXM (20 yanvar m/s)','28 May filialı (Qış parkı)','Filial № 5 (Sahil m/s)','Mərkəz filialı','Salyan filialı',
'Ağcabədi filialı','Filial № 11 (Elmlər Akademiyası m/s)','Filial Nərimanov','Filial № 4 (Xalqlar Dostluğu m/s)','Mərdəkan filialı',
'Filial Sədərək TM','Filial Sumqayıt','Filial Gəncə','Filial Bərdə','Filial Lənkəran']
choices3=['Kartın növünü seçin', 'Visa', 'Mastercard']

class LoanRequest1(FlaskForm):
    first_name = StringField(label="Ad", validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField(label="Soyad", validators=[DataRequired(), Length(min=3, max=30)])
    job = StringField(label="Iş yeri", validators=[DataRequired(), Length(min=3, max=30)])
    prefix = SelectField(choices=choices1)
    p_number = StringField(label="Mobil nömrə", validators=[DataRequired(), Length(min=3, max=30)])

class CardRequest(FlaskForm):
    card = SelectField(label="Kartın növünü seçin", choices=choices3)
    first_name = StringField(label="Ad", validators=[DataRequired(), Length(min=3, max=30)])
    last_name = StringField(label="Soyad", validators=[DataRequired(), Length(min=3, max=30)])
    prefix = SelectField(choices=choices1)
    p_number = StringField(label="Mobil nömrə", validators=[DataRequired(), Length(min=3, max=30)])
    code = StringField(label="Kod sözü", validators=[DataRequired(), Length(min=3, max=30)])
    branch = SelectField( choices=choices2)
    file1 = FileField()
    file2 = FileField()