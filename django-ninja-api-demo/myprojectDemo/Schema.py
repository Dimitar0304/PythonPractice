from ninja import Schema

from .api import api

class UserIn(Schema):
    username: str
    password: str


@api.post("/users/")
def create_user(request, data: UserIn):
    user = user(username=data.username) # User is django auth.User
    user.set_password(data.password)
    user.save()
    # ... return ?
    
