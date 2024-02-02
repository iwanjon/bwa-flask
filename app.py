from http.client import HTTPException
from flask import Flask, jsonify
from marshmallow import ValidationError
# from flask_restful import Api
# from flask_jwt_extended import JWTManager

from db import db
from ma import ma
# from blocklist import BLOCKLIST
# from resources.user import UserRegister, UserLogin, User, TokenRefresh, UserLogout
# from resources.user import AllUser, CheckEmailAvalilable, UserLogin, UserRegister,  User
from app_conf import app_config

######################

####################
app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.config["PROPAGATE_EXCEPTIONS"] = True
# app.secret_key = "jose"  # could do app.config['JWT_SECRET_KEY'] if we prefer
# api = Api(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()
# jwt = JWTManager(app)


# This method will check if a token is blocklisted, and will be called automatically when blocklist is enabled
# @jwt.token_in_blocklist_loader
# def check_if_token_in_blocklist(jwt_header, jwt_payload):
#     return jwt_payload["jti"] in BLOCKLIST


# api.add_resource(UserRegister, "/register")
# api.add_resource(UserLogin, "/login")
# api.add_resource(AllUser, "/user")
# api.add_resource(CheckEmailAvalilable, "/emailavalilablity")
# api.add_resource(User, "/user/<int:user_id>")
# api.add_resource(UserLogin, "/login")
# api.add_resource(TokenRefresh, "/refresh")
# api.add_resource(UserLogout, "/logout")
app_config(app)
# db.init_app(app)


@app.errorhandler(ValidationError)
def handle_marshmallow_validation(err):
    print(err, "dammint", type(err).__name__, type(err))

    return jsonify(
        message=err.messages,
        category="error",
        status=400
    )


@app.errorhandler(Exception)
def handle_marshmallow_validation(err):
    print(err, "dammint", type(err))
    # return jsonify(message=err), 400
    return jsonify(
        message="internal server error",
        category="error",
        status=500
    )


if __name__ == "__main__":

    ##################

    ################

    with app.app_context():
        db.create_all()
    ma.init_app(app)
    app.run(port=5000, debug=True)
