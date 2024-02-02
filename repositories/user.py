from typing import Dict, List
from models.user import UserModel
from db import db
import bcrypt

# type Repository interface {
# 	Save(user User) (User, error)
# 	FindByEmail(email string) (User, error)
# 	FindById(id int) (User, error)
# 	Update(user User) (User, error)
# 	FindAllUsers() ([]User, error)
# }

class UserRepository():
    def __init__(self,userModel:UserModel=None , userLogin:Dict = None):
        self.userModel = userModel
        self.userLogin = userLogin
        
    def add_user(self):
        db.session.add(self.userModel)
        
    def remove_user(self):
        db.session.delete(self.userModel)
        # self.userModel.delete(data)
    @classmethod
    def update_user(cls, user):
        db.session.add(user)
    
    def save_user(self):
        db.session.commit()
        # self.UserModel.commit()
    # def find_by_name(self):
    def set_hash_paword(self):
        salt = bcrypt.gensalt()
        # awal =  self.userModel.password
        po = bcrypt.hashpw(self.userModel.password.encode('utf-8'), salt)
        # po.decode('utf-8')
        # print(type(po))
        self.userModel.password = po.decode('utf-8')
        # result = bcrypt.checkpw(awal.encode('utf-8'), po)
  
        # print(result)
        # print(self.userModel.password, "string", self.userModel.password ,
        #       str(self.userModel.password),
        #       type(self.userModel.password),
        #     #   type(po.decode('utf-8')),
        #       str(self.userModel.password).encode('utf-8'))
        
    @classmethod
    def find_by_name(cls, name:str)->"UserModel":
        return db.session.query(UserModel).filter_by(name=name).first()
    
    @classmethod
    def find_by_email(cls, email:str)->"UserModel":
        return db.session.query(UserModel).filter_by(email=email).first()
      
    @classmethod
    def find_by_id(cls, id:int)->"UserModel":
        return db.session.query(UserModel).filter_by(id=id).first()
    
    @classmethod
    def find_all(cls)->"List(UserModel)":
        try:
            ret=  db.session.query(UserModel).all()
            print(ret, "eeeeeeeeeeeeeeee")
            return ret
        except  Exception as e:
            print(e)
            return []
    
    