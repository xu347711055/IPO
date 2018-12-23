from . import db
from sqlalchemy.dialects.mysql import INTEGER, VARCHAR, TINYINT


class User(db.Model):
    gkey = db.Column(INTEGER(unsigned=True), primary_key=True)
    name = db.Column(VARCHAR(30), unique=True, nullable=False)
    email = db.Column(VARCHAR(100))
    enabled = db.Column(TINYINT(unsigned=True), nullable=False)
    admin = db.Column(TINYINT(unsigned=True))

    # def __init__(self, name, email, enabled, admin):
    #     self.name = name
    #     self.email = email
    #     self.enabled = enabled
    #     self.admin = admin

    def __repr__(self):
        return '<User %r>' % self.username


class Task(db.Model):
    id = db.Column(INTEGER(unsigned=True), primary_key=True)
    task_nbr = db.Column(VARCHAR(100), unique=True, nullable=False)
