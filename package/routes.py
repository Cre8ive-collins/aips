from flask import render_template, url_for, flash, request, redirect
from package.forms import LoginForm
from package import app, db, bcrypt
from package.dbmodels import User, Admin, Tracks, Path, Post
import datetime
from flask_login import login_user      


post = {'tag':'<html>',
        'description': 'HTML5 tag blah blah blah',
        'date' : str(datetime.datetime.today()).split()[0]
        }


@app.route('/', methods=('GET','POST'))
def home():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            flash(f'Login Successfull','success')
            login_user(user, remember=remember)
            return redirect(url_for('home'))
        else:
            flash(f'Username or Password incorrect','warning')
    return render_template('login.html', form=form)

@app.route('/register', methods=('POST','GET'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        validate_email = User.query.filter_by(email=email).first()
        if validate_email:
            flash(f'Account already exist for {email}. Sign-in instead','danger')
            return render_template('register.html')
        username = request.form['username']
        validate_username = User.query.filter_by(username=username).first()
        if validate_username:
            flash(f'Username {username} already exist please select another username','warning')
            return render_template('register.html')
        password = request.form['password']
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, username=username, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {name}','success')
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/admin', methods=('POST','GET'))
def admin(): 
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        admin = Admin.query.filter_by(username=username).first()
        if admin and (password == admin.password):
            flash(f'Welcome {username}, what will you like to do?','success')
            login_user(admin, remember=remember)
            return render_template('admin.html', user=admin)
        else:
            flash(f'Username or Password incorrect','warning')
            #change template
    return render_template('admin.html', form=form)

@app.route('/post')
def posts():
    return render_template('post.html', post = post)