from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length, Email


class RegistrationForm(FlaskForm):
    fullname = StringField('fullname', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[
                             DataRequired(), Length(min=6, max=20)])
    confirmPassword = PasswordField('confirmPassword', validators=[
                                    DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
