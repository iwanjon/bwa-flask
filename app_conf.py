from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.campaign import CreateCampaign, SingleCampaign

from db import db
# from ma import ma
from resources.user import (AllUser, CheckEmailAvalilable, UserLogin, UserRegister,  User, UploadUserImage,
                            ServeUserImage, STATIC_IMAGE_URI)
# @app.errorhandler(ValidationError)
# def handle_marshmallow_validation(err):
#     return jsonify(err.messages), 400


def app_config(app: Flask):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    # could do app.config['JWT_SECRET_KEY'] if we prefer
    app.secret_key = "jose"
    errors = {
        'ValidationError': {
            'message': "A user with that username already exists.",
            'status': 409,
        },
        'ResourceDoesNotExist': {
            'message': "A resource with that ID no longer exists.",
            'status': 410,
            'extra': "Any extra information you want.",
        },
    }
    api = Api(app, catch_all_404s=True, errors=errors)
    # api = Api(app, catch_all_404s=True)
    db.init_app(app)
    jwt = JWTManager(app)

    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(AllUser, "/user")
    api.add_resource(CheckEmailAvalilable, "/emailavalilablity")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UploadUserImage, "/upload/<int:user_id>")
    api.add_resource(ServeUserImage, "/" +
                     STATIC_IMAGE_URI + "<string:filename>")
    api.add_resource(CreateCampaign, "/campaign")
    api.add_resource(SingleCampaign, "/campaign/<int:campaign_id>")
    # api.add_resource(UpdateCampaign, "/campaign/<int:campaign_id>")
    # return app
# if __name__ == "__main__":
#     db.init_app(app)
#     with app.app_context():
#         db.create_all()
#     ma.init_app(app)
#     app.run(port=5000, debug=True)
