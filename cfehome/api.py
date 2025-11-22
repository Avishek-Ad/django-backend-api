from ninja import Schema
from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

import helpers

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)
api.add_router("/waitlists/", "waitlists.api.router")

class UserSchema(Schema):
    username:str
    is_authenticated:bool
    email:str = None

@api.get("/hello/")
def hello(request):
    print(request)
    return {"message":"Hello world"}

# @api.get("/me/", response=UserSchema, auth=JWTAuth())
# def me(request):
#     return request.user

@api.get("/me/", response=UserSchema, auth=helpers.api_auth_user_required)
def me(request):
    user = request.user
    return {
        "username": user.username,
        "email": user.email,
        "is_authenticated": user.is_authenticated,
    }