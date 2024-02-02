# from unittest import TestCase
from .base_test import Basetest
from models.user import UserModel
from models.campaign import CampignModel
from repositories.user import UserRepository
from repositories.campaign import CampaignRepository 


class TestCampaignIntegration(Basetest):
    def test_campaign(self):
        with self.app_context():
            user = UserModel(
                    name = "user1",
                    occupation = "user1ocu",
                    email = "user1@gmail.com",
                    password = 1234,
                    role = "admin"
            )
            
            campaign_model = CampignModel(
                name = "campaign1",
                short_description = "short_campaign_1",
                description = "description_campaign",
                perks = "perks",
                slug = "seluk",
                backer_count = 12,
                goal = 120000000,
                current_amount = 12000
            )
            
            userModel= UserRepository(userModel= user)
            userModel.add_user()
            user_data = UserRepository.find_by_name("user1")
            
            campaign_model.user_id = user_data.id
            CampaignRepository.add_campaign(campaign_model)
            CampaignRepository.commit_campaign()
            
            self.assertEqual(CampaignRepository.get_campaign_by_id(1), campaign_model)
            
            self.assertEqual(CampaignRepository.get_campaign_by_id(1).user_id, user_data.id)
            
            self.assertEqual(len(CampaignRepository.get_all_campaign()) , 1)
            
            self.assertEqual(len(CampaignRepository.get_campaigns_by_userid(1))  , 1)
            
            
            

            
            
        