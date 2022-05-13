from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import Length, InputRequired


class ProfileForm(FlaskForm):
    username = StringField("Имя пользователя", validators=[InputRequired(), Length(min=5, max=32)])
    password = PasswordField("Пароль", validators=[InputRequired(), Length(min=9, max=24)])
    about_me = TextAreaField("О себе")
    submit = SubmitField("Принять")
