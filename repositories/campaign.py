from typing import List
from db import db
from models.campaign import CampignImageModel, CampignModel
from helper.error import NewError
# type Repository interface {
# 	FindAll() ([]Campaign, error)
# 	FindByUserId(userId int) ([]Campaign, error)
# 	FindById(id int) (Campaign, error)
# 	Save(campaign Campaign) (Campaign, error)
# 	Update(campaign Campaign) (Campaign, error)
# 	SaveImage(campaignImages CampaignImage) (CampaignImage, error)
# 	MarkAllImagesAsNonPrimary(campaignid int) (bool, error)
# }
class CampaignRepository():
    @classmethod
    def get_campaign_by_id(cls, campaign_id)->"CampignModel":
        return db.session.query(CampignModel).filter_by(id=campaign_id).first()
    
    @classmethod
    def get_campaigns_by_userid(cls, user_id)->List[CampignModel]:
        ret:List(CampignModel) =  db.session.query(CampignModel).filter_by(user_id=user_id).all()
        return ret
        
    @classmethod
    def get_all_campaign(cls)->"List(CampignModel)":
        return db.session.query(CampignModel).all()
    
    @classmethod
    def add_campaign(cls, campaignModel:CampignModel):
        db.session.add(campaignModel)
        
    @classmethod
    def commit_campaign(cls):
        db.session.commit()
        
    @classmethod
    def save_campaign_image(cls, campaignImage:CampignImageModel):
        db.session.add(campaignImage)
        
    @classmethod
    def mark_all_images_to_no_primary(cls, campaignid):
        all_campaign:List(CampignModel) = db.session.query(CampignModel).filter(CampignModel.id == campaignid).all()
        try:
            for i in all_campaign:
                i.is_primary = 0
                db.session.add(i)
            db.commit()
        except NewError as e:
            e.NewMessage = "error mark as non primary"
            raise e