import os
from flask_restful import Resource
from flask import request, send_from_directory
from hmac import compare_digest
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required,
    get_jwt,
)
from helper.error import NewError
from helper.responseFormatter import response_formatter, response_formatter_all
from marshmallow import ValidationError
from models.user import UserModel
from schemas.user import UserSchema, UserLoginSchema, EmailAvaliableSchema
from services.user import UserService
from werkzeug.utils import secure_filename
# from blocklist import BLOCKLIST

USER_ALREADY_EXISTS = "A user with that username already exists."
CREATED_SUCCESSFULLY = "User created successfully."
USER_NOT_FOUND = "User not found."
USER_DELETED = "User deleted."
INVALID_CREDENTIALS = "Invalid credentials!"
USER_LOGGED_OUT = "User <id={user_id}> successfully logged out."

user_schema = UserSchema()
user_login_schema = UserLoginSchema()
email_avaliable_schema = EmailAvaliableSchema()
STATIC_IMAGE_URI = "upload/"


class UserRegister(Resource):
    @classmethod
    def post(cls):
        # raise Exception("Sorry, no numbers below zero")
        user_data = user_schema.load(request.get_json())
        # try:
        #     user_data = user_schema.load(request.get_json())
        #     # import pdb
        #     # pdb.set_trace()
        # except ValidationError as err:
        #     print(err, "error in try")
        #     return err.messages, 400

        # if UserModel.find_by_name(user_data.name):
        #     return {"message": USER_ALREADY_EXISTS}, 400

        # user = UserModel(**user_data)
        # user_data.save_to_db()
        userService = UserService(userModel=user_data)
        try:
            userService.register_user()
        except NewError as e:
            print(e, ":error new resourse register")
            return {"message": e.NewMessage}, 400
        except Exception as e:
            print(e, ":error resourse register")
            return {"message": "error register user"}, 400
        return {"message": CREATED_SUCCESSFULLY}, 201


class UserLogin(Resource):
    @classmethod
    def post(cls):
        try:
            user_data = user_login_schema.load(request.get_json())
            print(user_data, type(user_data))
        except ValidationError as err:
            return err.messages, 400

        userService = UserService(userLogin=user_data)
        try:
            token = userService.login_user()
        except NewError as e:
            print(e, ":error new resourse login")
            return {"message": e.NewMessage}, 400
        except Exception as e:
            print(e, ":error resourse unkown login")
            return {"message": "error login user"}, 400
        return response_formatter("sukses", 200, "sukses", token), 200


class AllUser(Resource):
    @classmethod
    @jwt_required()
    def get(cls):
        users = UserService.get_all_user()
        return response_formatter_all("sukses", 201, "sukses", users, user_schema), 200


class CheckEmailAvalilable(Resource):
    @classmethod
    def post(cls):
        try:
            email = email_avaliable_schema.load(request.get_json())
        except ValidationError as err:
            return err.messages, 400
        exist = UserService.check_email(email["email"])
        if exist:
            return response_formatter("sukses", 200, "sukses", "email is registered"), 200

        return response_formatter("sukses", 200, "sukses", "email free to used"), 200


class User(Resource):
    @classmethod
    def get(cls, user_id: int):
        # user = UserModel.find_by_id(user_id)
        # if not user:
        #     return {"message": USER_NOT_FOUND}, 404
        existing_user = UserService.get_user_by_id(user_id)
        if not existing_user:
            return {"message": USER_NOT_FOUND}, 404
        return user_schema.dump(existing_user), 200

    @classmethod
    def delete(cls, user_id: int):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {"message": USER_NOT_FOUND}, 404

        user.delete_from_db()
        return {"message": USER_DELETED}, 200

    @classmethod
    def put(cls, user_id: int):
        try:
            user_data = user_schema.load(request.get_json())
            user_data.id = user_id
            # import pdb
            # pdb.set_trace()
        except ValidationError as err:
            return err.messages, 400
        userService = UserService(userModel=user_data)
        try:
            updated_user = userService.update_user()
        except NewError as e:
            print(e, ":error new resourse update")
            return {"message": e.NewMessage}, 400
        except Exception as e:
            print(e, ":error resourse unkown update")
            return {"message": "error login user"}, 400
        return response_formatter("update sukses", 201, "sukses", user_schema.dump(updated_user)), 201
        # return {"message": user_schema.dump(updated_user)}, 201


class UploadUserImage(Resource):
    @classmethod
    def post(cls, user_id: int):
        # check if the post request has the file part
        # print(request.host_url, request.host)
        image_uri = request.host_url + STATIC_IMAGE_URI
        if 'file' not in request.files:
            # flash('No file part')
            return {"message": "error in upload file"}, 400
        uploaded_file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if uploaded_file.filename == '':
            # flash('No selected file')
            return {"message": "error in upload filename"}, 400
        if not uploaded_file or not cls.allowed_file(uploaded_file.filename):
            return {"message": "error in upload filename"}, 400

        is_exist_user = UserService.get_user_by_id(user_id=user_id)
        if not is_exist_user:
            return {"message": "error in upload filename user"}, 400

        try:
            filename = UserService.upload_file(uploaded_file=uploaded_file)
        except NewError as e:
            return {"message": e.NewMessage}, 400

        # filename = secure_filename(uploaded_file.filename)
        # dirname = os.path.dirname(__file__)
        # uploaded_file.save(os.path.join(dirname,"..","images",filename))
        userService = UserService(
            userImageName=image_uri+filename, userModel=is_exist_user)
        userService.update_user()
        return response_formatter("upload sukses", 201, "sukses", "upload sukses"), 201

    @classmethod
    def allowed_file(cls, filename):
        ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
        return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class ServeUserImage(Resource):
    @classmethod
    def get(cls, filename):
        dirname = os.path.dirname(__file__)
        return send_from_directory(os.path.join(dirname, "..", "images"), filename)
