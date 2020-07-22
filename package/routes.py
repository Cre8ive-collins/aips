from flask import render_template, url_for, flash, request, redirect
from package.forms import LoginForm
from package import app, db, bcrypt
from package.dbmodels import User, Admin, Tracks, Path, Post
from flask_login import login_user, current_user, logout_user, login_required      
from itertools import chain




@app.route('/', methods=('GET','POST'))
def home():
    track = Tracks.query.all()
    return render_template('index.html', track = track)

@app.route('/intro/<id>')
def intro(id):
    track = Tracks.query.get(id)
    path = Path.query.filter_by(track = 1).all()
    return render_template('intro.html', track = track, path = path)

@app.route('/register', methods=('POST','GET'))
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        validate_email = User.query.filter_by(email=email).first()
        if validate_email:
            flash(f'Account already exist for {email}. Sign-in instead','warning')
            return render_template('register.html')
        username = request.form['username']
        phone = request.form['phone']
        validate_username = User.query.filter_by(username=username).first()
        if validate_username:
            flash(f'Username {username} already exist please select another username','warning')
            return render_template('register.html')
        password = request.form['password']
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(name=name, email=email, username=username, password=hashed_pw,phone= phone)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {name}','success')
        return redirect(url_for('home'))
    return render_template('register.html')


@app.route('/admin', methods=('POST','GET'))
def admin():
    form = LoginForm()
    # students = max(list(chain(*User.query.with_entities(User.id).all())))
    # lesson = max(list(chain(*Admin.query.with_entities(Admin.id).all())))
    # path = max(list(chain(*Path.query.with_entities(Path.id).all())))
    # track = max(list(chain(*Tracks.query.with_entities(Tracks.id).all())))
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        admin = Admin.query.filter_by(username=username).first()
        if admin and (password == admin.password):
            flash(f'Welcome {username}, what will you like to do?','success')
            login_user(admin)
            return render_template('admin.html', form = form)
        else:
            flash(f'Username or Password incorrect','warning')
            return render_template('admin_login.html', form=form)

    return render_template('admin_login.html', form=form)

@app.route('/create_post', methods = ('POST','GET'))
def create_post():
    admin = list(chain(*Admin.query.with_entities(Admin.username).all()))
    path = list(chain(*Path.query.with_entities(Path.title).all()))
    track = list(chain(*Tracks.query.with_entities(Tracks.title).all()))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        body = request.form['body']
        subject = request.form['subject']
        track = request.form['track']
        video = request.form['video']
        author = request.form['author']
        authors_password = request.form['authors_password']
        validate_creator = Admin.query.filter_by(username = author).first()
        if validate_creator.password == authors_password:
            post = Post(title = title, description = description, body= body, subject = subject, track = track, creator = author, video = video)
            db.session.add(post)
            db.session.commit()
            flash(f"Post {title} created", "success")
            return render_template('layout.html')
        else:
            flash(f"Post {title}  could not be created as admin password is not correct", "danger")
    return render_template("create_post.html",path = path, track = track, admin = admin)

@app.route('/read_user_form', methods = ('POST',))
def read_user_form():
    entry = request.form['read_user']
    first_user = list(User.query.filter_by(username = entry))
    all_user = User.query.all()
    if first_user:
        flash(f'first', 'warning')
        return render_template('admin.html', read_user = first_user)
    if entry == 'all':
        flash(f'all', 'warning')
        first_user = list(User.query.all())
        return render_template('admin.html', read_user = all_user)
    
    elif not first_user:
        first_via_email = list(User.query.filter_by(email = entry))
        if not first_via_email:
            flash(f'{entry} is not registered', 'warning')
            return render_template('admin.html')
        flash(f'first_via_email', 'warning')
        return render_template('admin.html', read_user = first_via_email)
    else:
        flash(f'{entry} is not registered', 'warning')
        return render_template('admin.html')
    
@app.route('/add_course', methods = ('POST',) )
def add_course():
    if request.method == 'POST':
        track = request.form['create_track']
        course = request.form['create_course']
        if course == "":
            tracks = Tracks.query.filter_by(title = track)
            if tracks:
                flash(f'Track already exist','warning')
                return redirect(url_for('admin'))
            else:
                tra = Tracks(title = track).first()
                db.session.add(tra)
                db.session.commit()
                flash(f'Track {track} created', 'success')
                return redirect(url_for('admin'))

        else:
            courses = Path.query.filter_by(title = course).first()
            if courses:
                flash(f'Course already exist','warning')
                return redirect(url_for('admin'))
            else:
                tracks = Tracks.query.filter_by(title = track)
                if not tracks:
                    tra = Tracks(title = track).first()
                    path = Path(track = track, title = course)
                    db.session.add(path)
                    db.session.add(tra)
                    db.session.commit()
                    db.session.commit()
                    flash(f'Course {course} created', 'success')
                    return redirect(url_for('admin'))
                else:
                    path = Path(track = track, title = course)
                    db.session.add(path)
                    db.session.commit()
                    flash(f'Course {course} created', 'success')
                    return redirect(url_for('admin'))

@app.route('/studycenter/<title>/<id>')
def studycenter(title, id = 1):
    post = Post.query.filter_by(subject = title).all()
    if id == "all":
        if post == []:
            return "ERROR"
        return render_template ('all.html', post = post)
    else:
        current_post = Post.query.get_or_404(id)
        return render_template ('studycenter.html', post = post, current_post = current_post)

@app.route('/html/<post_id>')
def html(post_id):
    post = Post.query.filter_by(subject = 'HTML').all()
    current_post = Post.query.get_or_404(post_id)
    return render_template('html.html', post = post, current_post = current_post)


@app.route('/css/<post_id>')
def css(post_id):
    post = Post.query.filter_by(subject = 'CSS').all()
    current_post = Post.query.get_or_404(post_id)
    return render_template('css.html', post = post, current_post = current_post)

@app.route('/javascript/<post_id>')
def javascript(post_id):
    post = Post.query.filter_by(subject = 'javascript').all()
    current_post = Post.query.get_or_404(post_id)
    return render_template('javascript.html', post = post, current_post = current_post)


@app.route('/bootstrap/<post_id>')
def bootstrap(post_id):
    post = Post.query.filter_by(subject = 'bootstrap').all()
    current_post = Post.query.get_or_404(post_id)
    return render_template('html.html', post = post, current_post = current_post)


@app.route('/jquery/<post_id>')
def jquery(post_id):
    post = Post.query.filter_by(subject = 'jquery').all()
    current_post = Post.query.get_or_404(post_id)
    return render_template('jquery.html', post = post, current_post = current_post)

@app.route('/login',  methods = ('POST', 'GET'))
def login():
    if current_user.is_authenticated:
        return redirect( url_for('home') )
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        user = User.query.filter_by(username=username).first()
        if user:
            checked_pw = bcrypt.check_password_hash(user.password, form.password.data)
            if checked_pw:
                flash(f'Welcome {username}, what will you like to do?','success')
                login_user(user)
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                else:
                    return redirect(url_for('home') )
        else:
            flash(f'Username or Password incorrect','danger')

    return render_template('login.html', form = form)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account')
def account():
    return render_template('account.html')

@app.route("/test")
def test():
    return render_template('testing.html')