import datetime
import os
import string
import tempfile
from typing import Dict, List
import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token
from models.user import UserModel
from repositories.user import UserRepository
from helper.error import NewError
from db import db
from datetime import datetime, timedelta
from werkzeug.utils import secure_filename
# import 

# type Service interface {
# 	RegisterUser(input RegisterUser) (User, error)
# 	LoginUser(input LoginInput) (User, error)
# 	CheckEmailAvailable(input CheckEmailInput) (bool, error)
# 	SaveAvatar(id int, filelocation string) (User, error)
# 	GetUserById(id int) (User, error)
# 	GetAllUsers() ([]User, error)
# 	UodateUser(i FormUpdateInput) (User, error)
# }

class UserService():
    # def __init__(self,UserRepository:UserRepository):
    #     self.UserRepository = UserRepository
    def __init__(self,userModel:UserModel=None, userLogin:Dict = None, userImageName:string= None):
        self.userRepository = UserRepository(userModel= userModel, userLogin = userLogin)
        self.userModel = userModel
        self.userLogin = userLogin
        self.userImageName = userImageName
        
    # def add_user(self):
    #     self.userRepository.add_user()
          
    # def remove_user(self):
    #     # db.session.delete(self.UserModel)
    #     # self.UserModel.delete(data)
    #     self.userRepository.remove_user()
        
    # def save_user(self):
    #     self.userRepository.save_user()
    #     # self.UserModel.commit()
        
        
    def register_user(self):
        existingUser = UserRepository.find_by_email(self.userModel.email)
        if existingUser:
            print("error email exist")
            error  =  NewError("email already exist")
            # db.session.rollback()
            raise error
        self.userRepository.set_hash_paword()
        try:
            self.userRepository.add_user()
            self.userRepository.save_user()
        except Exception as e:
            error  =  NewError(e)
            db.session.rollback()
            raise error
    
    def login_user(self):
        existingUser = UserRepository.find_by_email(self.userLogin["email"])
        if not existingUser:
            print("error email do not exist")
            error  =  NewError("email do not exist")
            # db.session.rollback()
            raise error 
        print(":is true", existingUser.password)
        
        existing_password = existingUser.password.encode("utf-8")
        result = bcrypt.checkpw(self.userLogin["password"].encode("utf-8"), existing_password)
        print(result, ":is true", existing_password)
        if not result:
            print("error password do not match")
            error  =  NewError("password do not match")
            # db.session.rollback()
            raise error 
        
        aceess_token = create_access_token(fresh=True, expires_delta= timedelta(minutes=30), identity=existingUser.id)
        refresh_token = create_refresh_token(expires_delta= timedelta(minutes=30), identity=existingUser.id)
        return {"aceess_token":aceess_token, "refresh_token":refresh_token}       
    
    def update_user(self):
        existingUser = UserRepository.find_by_id(self.userModel.id)
        if not existingUser:
            print("error id do not exist")
            error  =  NewError("user do not exist")
            # db.session.rollback()
            raise error 
        existingUser.updated_at = datetime.now()
        existingUser.email = self.userModel.email
        existingUser.name = self.userModel.name
        existingUser.occupation = self.userModel.occupation
        if self.userImageName:
            existingUser.avatar_filename = self.userImageName
        try:
            UserRepository.update_user(existingUser)
            self.userRepository.save_user()
        except Exception as e:
            error  =  NewError(e)
            db.session.rollback()
            raise error
        return existingUser 
    
    @classmethod
    def get_user_by_id(cls, user_id)->UserModel:
        existing = UserRepository.find_by_id(user_id)
        return existing
    
    @classmethod
    def get_all_user(cls) -> "List(UserModel)":
        all_existing = UserRepository.find_all()
        # if all_existing == []:
        return all_existing
        # for 
    @classmethod
    def check_email(cls, email) -> bool:
        existing = UserRepository.find_by_email(email)
        if existing:
            return True
        return False
    
    @classmethod
    def upload_file(cls, uploaded_file):
        try:
            filename = secure_filename(uploaded_file.filename)
            dirname = os.path.dirname(__file__)
            tf = tempfile.NamedTemporaryFile()
            last_tf = tf.name.split("\\")[-1]
            last_tf +=  filename
            uploaded_file.save(os.path.join(dirname,"..","images",last_tf))
        except NewError as e:
            e.NewMessage="error in uploaded file"
            raise e

        return last_tf