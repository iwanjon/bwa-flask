# from unittest import TestCase
from .base_test import Basetest
from models.user import UserModel
from repositories.user import UserRepository


class TestUserIntegrationTest(Basetest):
    def createuser(self):
        with self.app_context():
            user = UserModel(
                    name = "user1",
                    occupation = "user1ocu",
                    email = "user1@gmail.com",
                    password = 1234,
                    # avatar_filename = "user1avatar",
                    role = "admin",
                    # campaign ="campaign"
            )
            userModel= UserRepository(userModel= user)
            userModel.add_user()
            self.assertEqual(UserRepository.find_by_name("user1"), user)
            
            userModel.remove_user()
            self.assertIsNone(UserRepository.find_by_name("user1"))
        