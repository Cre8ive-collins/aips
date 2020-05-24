
from package import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60),nullable=False)

    def __repr__(self):
        return f"User('{self.id}, {self.name}, {self.email}, {self.username}')"    

class Admin(db.Model, UserMixin):
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(60),nullable=False)
    rele = db.relationship('Post', backref = 'author', lazy = True)

    def __repr__(self):
        return f"Admin('{self.id}, {self.name}, {self.email}, {self.username}')"    

class Tracks(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text )
    rel = db.relationship('Path', backref = 'line', lazy = True)
    rel = db.relationship('Post', backref = 'line', lazy = True)

    def __repr__(self):
        return f"Track('Track Number = {self.id}, Title = {self.title}')"

class Path(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    track = db.Column(db.Integer, db.ForeignKey('tracks.id'), nullable=False)
    rela = db.relationship('Post', backref = 'course', lazy=True)

    def __repr__(self):
        return f"Course({self.title},{self.track})"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.Text, nullable = False)
    description = db.Column(db.Text, nullable = False)
    body = db.Column(db.Text, nullable = False)
    subject = db.Column(db.Integer, db.ForeignKey('path.id'), nullable=False)
    creator = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    track = db.Column(db.Integer, db.ForeignKey('tracks.id'))
    image = db.Column(db.String)
    video = db.Column(db.String)

    def __repr__(self):
        return f"{self.title},{self.description},{self.author}"
    
