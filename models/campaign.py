# package campaign

# import (
# 	"bwastartup/user"
# 	"time"

# 	"github.com/leekchan/accounting"
# )



# type Campaign struct {
# 	ID               int
# 	UserID           int
# 	Name             string
# 	ShortDescription string
# 	Description      string
# 	Perks            string
# 	BackerCount      int
# 	GoalAmount       int
# 	CurrentAmount    int
# 	Slug             string
# 	CreatedAt        time.Time
# 	UpdatedAt        time.Time
# 	CampaignImages   []CampaignImage
# 	User             user.User
# }

# // func (cam *Campaign) GoalAmountFormatIDR() string {

# // 	return "formater.FormatMoney(cam.GoalAmount)"
# // }



from typing import Dict, List, Union
from db import db
from datetime import datetime
# from .user import UserModel

itemJson = dict[str, Union[int,str,float]]

class CampignModel(db.Model):
    __tablename__ = "campaigns"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String(80), nullable=False)
    short_description = db.Column(db.String(80))
    description = db.Column(db.String(80))
    perks = db.Column(db.String(80))
    slug = db.Column(db.String(80))
    backer_count = db.Column(db.Integer)
    goal = db.Column(db.Integer)
    current_amount = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow )
    updated_at = db.Column(db.DateTime, default=datetime.utcnow )
    campaingimages = db.relationship("CampignImageModel", back_populates = "campaign", lazy = True)
    user = db.relationship("UserModel", back_populates = "campaign", lazy = True)

# type CampaignImage struct {
# 	ID         int
# 	CampaignID int
# 	FileName   string
# 	IsPrimary  int
# 	CreatedAt  time.Time
# 	UpdatedAt  time.Time
# }

class CampignImageModel(db.Model):
    __tablename__ = "campaign_images"

    id = db.Column(db.Integer, primary_key=True)
    campaign_id = db.Column(db.Integer, db.ForeignKey("campaigns.id"))
    file_name = db.Column(db.String(80), nullable=False)
    is_primary = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow )
    updated_at = db.Column(db.DateTime, default=datetime.utcnow )
    campaign = db.relationship("CampignModel", back_populates = "campaingimages", lazy = True)
