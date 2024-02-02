

# type Service interface {
# 	FindCampaigns(userId int) ([]Campaign, error)
# 	GetCampaignById(input GetCampaignDetailInput) (Campaign, error)
# 	CreateCampaign(input CreateCampaignInput) (Campaign, error)
# 	UpdateCampaign(inputID GetCampaignDetailInput, inputparam CreateCampaignInput) (Campaign, error)
# 	SaveCampaignImage(input CreateCampaignImageInput, filelocation string) (CampaignImage, error)
# }
from datetime import datetime
from typing import List
from helper.error import NewError
from models.campaign import CampignImageModel, CampignModel
from repositories.campaign import CampaignRepository
from slugify import slugify


class Campaignservice():
    @classmethod
    def get_campaign_by_id(cls, campaign_id)->CampignModel:
        return CampaignRepository.get_campaign_by_id(campaign_id)
    
    @classmethod
    def get_campaigns_by_userid(cls, user_id)->List[CampignModel]:
        return CampaignRepository.get_campaigns_by_userid(user_id)
    
    @classmethod
    def create_campaign(cls, campaign:CampignModel)-> CampignModel:
        campaign.slug =slugify(campaign.name + " "+str(campaign.goal))
        CampaignRepository.add_campaign(campaign)
        CampaignRepository.commit_campaign()
        return campaign
        
    @classmethod
    def update_campaign(cls, campaign:CampignModel):
        current_campaign = CampaignRepository.get_campaign_by_id(campaign.id)
        if not current_campaign:
            error = NewError("errror not found product")
            raise error
        current_campaign.backer_count = campaign.backer_count
        # current_campaign.campaingimages = campaign.campaingimages
        current_campaign.current_amount = campaign.current_amount
        current_campaign.description = campaign.description
        current_campaign.goal = campaign.goal
        current_campaign.name = campaign.name
        current_campaign.perks = campaign.perks
        current_campaign.short_description = campaign.short_description
        current_campaign.slug = campaign.slug
        current_campaign.updated_at = datetime.now()
        
        CampaignRepository.add_campaign(current_campaign)
        CampaignRepository.commit_campaign()
        return current_campaign
        
    @classmethod
    def save_campaign_image(cls, campaign_image:CampignImageModel):
        try:
            CampaignRepository.mark_all_images_to_no_primary(campaign_image.campaign_id)
            CampaignRepository.save_campaign_image(campaignImage=campaign_image)
            CampaignRepository.commit_campaign()
        except NewError as e:
            e.NewMessage = "error in save campaign images"
            raise e
        
    