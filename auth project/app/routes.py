from flask import render_template, redirect, url_for, flash
from app import app
from app.form import LoginForm

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.user.data, form.remember_me.data))
        return redirect(url_for('login'))
    return render_template('login.html', title='Sign In', form=form)