from datetime import datetime, timedelta, timezone

from .database import db

# from flask_security import RoleMixin, UserMixin


current_timeutc = datetime.now(timezone.utc)
ist_offset = timedelta(hours=5, minutes=30)
current_time = current_timeutc + ist_offset

# ? id, title, genre, played


class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    genre = db.Column(db.String(50))
    played = db.Column(db.Boolean, default=False)


# ---------------------------------------TOUR GUIDE----------------------------------
'''
class RolesUsers(db.Model):
    __tablename__ = 'roles_users'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column('user_id', db.Integer(), db.ForeignKey('user.id'))
    role_id = db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    active = db.Column(db.Boolean(), default=True)
    fs_uniquifier = db.Column(db.String(255), unique=True, nullable=False)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(100))
    current_login_ip = db.Column(db.String(100))
    login_count = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary='roles_users',
                            backref=db.backref('users', lazy='dynamic'))


class Destination(db.Model):
    pass


class Enquiry(db.Model):
    pass


class Day1Plan(db.Model):
    pass


class Day2Plan(db.Model):
    pass


class Day3Plan(db.Model):
    pass


class Day4Plan(db.Model):
    pass


class Day5Plan(db.Model):
    pass


class Day6Plan(db.Model):
    pass


class Day7Plan(db.Model):
    pass
'''
