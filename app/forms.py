from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired


class UserForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

class UpdateUserForm(FlaskForm):
    id = StringField('ID', validators=[InputRequired()])
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired()])

class DeleteUserForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired()])
