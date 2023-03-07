from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length


# Book Forms

class CreateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = SelectField('Author', validators=[DataRequired()])
    date_published = DateField(label='Date published', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Create')


class UpdateBookForm(FlaskForm):
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = SelectField('Author', validators=[DataRequired()])
    date_published = DateField(label='Date published', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Update')


class DeleteBookForm(FlaskForm):
    submit = SubmitField(label='Delete')


# Author Forms


class CreateAuthorForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=2, max=50)])
    birthdate = DateField(label='Date of birthday', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Create')


class UpdateAuthorForm(FlaskForm):
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=2, max=50)])
    birthdate = DateField(label='Date of birthday', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Update')


class DeleteAuthorForm(FlaskForm):
    submit = SubmitField(label='Delete')
