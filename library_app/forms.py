""" Forms file for library_app """
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


# Book Forms

class CreateBookForm(FlaskForm):
    """ Form of creating Book """
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = SelectField('Author', validators=[DataRequired()])
    date_published = DateField(label='Date published', validators=[DataRequired()], format='%Y-%m-%d')
    price = IntegerField(label='Price', validators=[DataRequired()])
    submit = SubmitField(label='Create')


class UpdateBookForm(FlaskForm):
    """ Form of updating Book """
    title = StringField(label='Title', validators=[DataRequired(), Length(min=2, max=50)])
    author = SelectField('Author', validators=[DataRequired()])
    date_published = DateField(label='Date published', validators=[DataRequired()], format='%Y-%m-%d')
    price = IntegerField(label='Price', validators=[DataRequired()])
    submit = SubmitField(label='Update')


class DeleteBookForm(FlaskForm):
    """ Form of deleting Book """
    submit = SubmitField(label='Delete')


class FilterBookForm(FlaskForm):
    """ Form of filtering Book by start and end date """
    date_published_start = DateField(label='Date published start', validators=[DataRequired()], format='%Y-%m-%d')
    date_published_end = DateField(label='Date published end', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Submit')


# Author Forms


class CreateAuthorForm(FlaskForm):
    """ Form of creating Author """
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=2, max=50)])
    birthdate = DateField(label='Date of birthday', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Create')


class UpdateAuthorForm(FlaskForm):
    """ Form of updating Author """
    first_name = StringField(label='First name', validators=[DataRequired(), Length(min=2, max=50)])
    last_name = StringField(label='Last name', validators=[DataRequired(), Length(min=2, max=50)])
    birthdate = DateField(label='Date of birthday', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField(label='Update')


class DeleteAuthorForm(FlaskForm):
    """ Form of deleting Author """
    submit = SubmitField(label='Delete')
