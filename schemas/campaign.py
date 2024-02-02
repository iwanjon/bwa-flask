from marshmallow import EXCLUDE 
from ma import ma, fields
from models.campaign import CampignModel
from models.user import UserModel
# from marshmallow import  fields

# ma.Schema
# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = UserModel
#         load_instance = True
#         load_only = ("password",)
#         dump_only = ("id",)
class CampaignSchema(ma.Schema):
    class Meta:
        unknown = EXCLUDE
        model = CampignModel
        load_instance = True
        # load_only = ("password",)
        dump_only = ("id",)




# class UserLoginSchema(ma.Schema):
#     class Meta:
#         unknown = EXCLUDE
#     email = fields.fields.Str(required=True)
#     password = fields.fields.Str(required=True)
    
# class EmailAvaliableSchema(ma.Schema):
#     class Meta:
#         unknown = EXCLUDE
#     email = fields.fields.Str(required=True)
#     # password = fields.fields.Str(required=True)
