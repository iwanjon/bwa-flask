from unittest import TestCase
from models.user import UserModel
from models.campaign import CampignModel

class TestUser(TestCase):
    def create_user(self):
        # campaign = CampignModel(user="user")
        user = UserModel(
                name = "user1",
                occupation = "user1ocu",
                email = "user1@gmail.com",
                password = 1234,
                # avatar_filename = "user1avatar",
                role = "admin",
                # campaign ="campaign"
        )
        self.assertEqual(user.role, "admin")
        self.assertNotEqual(user.role, "amin")