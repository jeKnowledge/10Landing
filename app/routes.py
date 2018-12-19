from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm, ContactForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    cena = "Wow! Que cena fixe"
    return render_template('about.html', cena=cena)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash("Contact form sent! Thank you {}".format(form.name.data))
        return redirect(url_for('index'))
    return render_template('contact.html', form=form)
