from unittest import TestCase
from models.user import UserModel
from models.campaign import CampignModel

class TestCampaign(TestCase):
    def create_user(self):   
        campaign  = CampignModel(
        # user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
        name = "campaign1",
        short_description = "short cam[paign]",
        description = "desc",
        perks = "string perk",
        slug = "slug",
        backer_count = 1,
        goal = 111111,
        current_amount = 11
        )
        self.assertEqual(campaign.name,"campaign1")