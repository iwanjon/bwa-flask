# package user

# import "time"

# type User struct {
# 	ID             int
# 	Name           string
# 	Occupation     string
# 	Email          string
# 	PasswordHash   string
# 	AvatarFileName string
# 	Role           string
# 	CreatedAt      time.Time
# 	UpdatedAt      time.Time
# }

from typing import Dict, List, Union
from db import db
from datetime import datetime
# from .campaign import CampignModel

itemJson = dict[str, Union[int,str,float]]

class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    occupation = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(255), nullable = False)
    avatar_filename = db.Column(db.String(80))
    role = db.Column(db.String(80), default = "user")
    created_at = db.Column(db.DateTime, default=datetime.utcnow )
    updated_at = db.Column(db.DateTime, default=datetime.utcnow )
    campaign = db.relationship("CampignModel", back_populates="user", lazy=True)

    # store_id = db.Column(db.Integer, db.ForeignKey("stores.id"))
    # store = db.relationship("StoreModel", back_populates="items")

    # def __init__(self, name:str, , ):
    #     self.name = name
    #     self.price = price
    #     self.store_id = store_id

    # def json(self)-> itemJson:
    #     return {
    #         "id": self.id,
    #         "name": self.name,
    #         "price": self.price,
    #         "store_id": self.store_id,
    #     }

    @classmethod
    def find_by_name(cls, name:str)->"UserModel":
        return cls.query.filter_by(name=name).first()

    @classmethod
    def find_all(cls) ->List["UserModel"]:
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
