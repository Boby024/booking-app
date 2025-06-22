from dataclasses import dataclass


@dataclass
class AuthResponse:
    id: str = None
    email: str = None
    username: str = None
    token: str = None
    msg_: str = None

    def serialize(self):
        return {
            "id": str(self.id),
            "email": self.email,
            "username": self.username,
            "token": self.token,
            "msg_": self.msg_
        }
