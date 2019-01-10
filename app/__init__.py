from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
admin = Admin(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    email = db.Column(db.String(64))
    phone = db.Column(db.Integer())
    zip = db.Column(db.Integer())

    def __repr__(self):
        return '<Contact {}>'.format(self.name)

admin.add_view(ModelView(Contact, db.session))

from app import routes
