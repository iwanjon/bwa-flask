from unittest import TestCase
from app import app
from db import db

class Basetest(TestCase):
    def setUp(self) :
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
        with app.app_context():
            db.init_app(app)
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context
        
    def tearDown(self) :
        with self.app_context():
            db.session.remove()
            db.drop_all()
        # pass
        