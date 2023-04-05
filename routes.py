import json
from app import app, base

from flask import render_template,\
    flash,\
    redirect,\
    url_for
    
from flask import session

from forms import LoginForm, RegisterForm

@app.route('/')
@app.route('/index/')
def index():
    if session.get('is_auth'):
        return render_template('index.html')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if session.get('is_auth'):
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        users = base.get("users")
        print(users)
        for user in users:
            if user.get('login') == form.login.data:
                break
        else:
            return redirect(url_for('login'))
        flash(f'Login {form.login.data}')
        session['is_auth'] = True
        
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if session.get('is_auth'):
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f'Registered {form.login.data}')
        
        users = base.get("users")
        
        users.append({
            'login' : form.login.data,
            'pwd' : form.password.data
        })
        
        save_database()
        
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


def save_database():
    with open('data/database.json', 'w') as file_base:
        json.dump(base, file_base, indent=4)