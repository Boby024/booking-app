from pydantic import BaseModel


class UserRegisterRequest():
    username: str
    password: str
    email: str
    # roles: list =  []
    firstname: str
    lastname: str
    # access_token: str

    class Config:
        orm_mode = True 

    def __init__(self, username, password, email, firstname, lastname):
        self.username = username
        self.password = password
        self.email = email
        # self.roles = roles
        self.firstname = firstname
        self.lastname = lastname

    def register_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            # "roles": self.roles,
            "firstname": self.firstname,
            "lastname": self.lastname
        }


class UserLoginRequest:
    username: str
    password: str
    email: str

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        
    def login_dict(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email
        }
