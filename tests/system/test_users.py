# from unittest import TestCase 
# from app import app
# import sys
# sys.path.append('../..')
import json
from services.user import UserService
from .base_test import BaseTest
#  (conda311) C:\Users\lenovo\Documents\personal\bwastartupflaskrestful\bwastartupflaskresful>python -m unittest -v tests.system.test_users.TestUser
#  (conda311) C:\Users\lenovo\Documents\personal\bwastartupflaskrestful\bwastartupflaskresful>python -m unittest 
class TestUser(BaseTest):
    def test_user(self):
        with self.app() as c:
            # with self.app_context():
            data = {
                    "name":"momom",
                    "occupation" :"occupation", 
                    "email": "momom@gmail.com",
                    "password":"1234"
                    }
            resp = c.post("/register", json = data)
            print(resp.status_code, "response")
            self.assertEqual(resp.status_code, 201)
            
            self.assertEqual(UserService.get_user_by_id(1).name, data["name"])
            
            resp = c.post("/register", json = data)
            # print(resp.status_code, "response")
            # print(resp.data, "response")
            
            self.assertEqual({"message": "email already exist"}, json.loads(resp.data))
            resp = c.post("login", json={"email": data["email"], "password": data["password"]})
            print(resp.text)
            print(json.loads(resp.text))
            # response = c.get('/user')
            # print(response.text)
            # self.assertEqual(response.status_code,200)
            # resp = c.get("/user")
            resp = c.get("/user", headers = {"Authorization":"Bearer "+json.loads(resp.text)["data"]["aceess_token"]})
            print(resp.status_code, "response")
            print(resp.text, "response")
            self.assertEqual(resp.status_code, 200)
            