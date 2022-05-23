from project.ProfileForm import ProfileForm
from flask import Flask, render_template, request, redirect, url_for
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/', methods=['POST', 'GET'])
def index():
    form = ProfileForm()
    if form.validate_on_submit():
        username = form.username.data
        about_me = form.about_me.data
        password = form.password.data
        return render_template('index.html',
                               form=form,
                               username=username,
                               about_me=about_me,
                               password=password)
    else:
        return render_template('index.html', form=form)
