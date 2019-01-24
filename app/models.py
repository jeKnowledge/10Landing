from flask_admin.contrib.sqla import ModelView
from app import db, admin

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(64))
    phone = db.Column(db.Integer())
    zip = db.Column(db.Integer())

    def __repr__(self):
        return '<Contact {}>'.format(self.name)

admin.add_view(ModelView(Contact, db.session))
