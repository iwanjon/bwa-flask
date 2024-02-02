from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
# from resources.user import  STATIC_IMAGE_URI
from db import db
from ma import ma
# from blocklist import BLOCKLIST
# from resources.user import UserRegister, UserLogin, User, TokenRefresh, UserLogout
from resources.user import (AllUser, CheckEmailAvalilable, UserLogin, UserRegister,  User, UploadUserImage,
                            ServeUserImage, STATIC_IMAGE_URI)

def run_this_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["JWT_TOKEN_LOCATION"] = ["headers"]
    app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
    api = Api(app)


    # @app.before_first_request
    # def create_tables():
    #     db.create_all()


    jwt = JWTManager(app)


    # This method will check if a token is blocklisted, and will be called automatically when blocklist is enabled
    # @jwt.token_in_blocklist_loader
    # def check_if_token_in_blocklist(jwt_header, jwt_payload):
    #     return jwt_payload["jti"] in BLOCKLIST


    api.add_resource(UserRegister, "/register")
    api.add_resource(UserLogin, "/login")
    api.add_resource(AllUser, "/user")
    api.add_resource(CheckEmailAvalilable, "/emailavalilablity")
    api.add_resource(User, "/user/<int:user_id>")
    api.add_resource(UploadUserImage, "/upload/<int:user_id>")
    api.add_resource(ServeUserImage, "/"+STATIC_IMAGE_URI +"<string:filename>")
    # api.add_resource(UserLogin, "/login")
    # api.add_resource(TokenRefresh, "/refresh")
    # api.add_resource(UserLogout, "/logout")


    db.init_app(app)
    with app.app_context():
        db.create_all()
    ma.init_app(app)
    # app.run(port=5000, debug=True)
    return app
