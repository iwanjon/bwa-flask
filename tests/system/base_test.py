from unittest import TestCase 
from app import app
from db import db
#  (conda311) C:\Users\lenovo\Documents\personal\bwastartupflaskrestful\bwastartupflaskresful>python -m unittest -v tests.system.test_users.TestUser
#  (conda311) C:\Users\lenovo\Documents\personal\bwastartupflaskrestful\bwastartupflaskresful>python -m unittest 
class BaseTest(TestCase):
    # def setUp(self):
    #     print( "the setup function")
    #     self.app = app.test_client
        # with app.test_client() as c:
            # response = c.get('/user')
            # print(response.text)
            # self.assertEqual(response.status_code,200)
    def setUp(self) :
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data2.db"
        with app.app_context():
            try:
                db.init_app(app)
            except:
                pass
            db.create_all()
        self.app = app.test_client
        self.app_context = app.app_context
        
    def tearDown(self) :
        with self.app_context():
            db.session.remove()
            db.drop_all()