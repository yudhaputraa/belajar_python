from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email



class Mahasiswa_F(FlaskForm):
    npm = StringField('NPM', validators=[DataRequired(), Length(min=10, max=15)])
    nama = StringField('Nama', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    kelas = StringField('Kelas', validators=[DataRequired()])
    alamat = TextAreaField('Alamat', validators=[DataRequired()])
    submit = SubmitField('Tambah')