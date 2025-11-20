from flask import request

from .users_model import list_all_users, find_user_by_id, User
from .users_schema import UserSchema
from ...utils.simple_errors import simple_errors

@simple_errors
def get_users():
    """Get all users"""
    users = list_all_users()
    users_json = UserSchema(many=True).dump(users)
    return users_json, 200

def get_user_by_id(id):
    try:
        user = find_user_by_id(id)
    except (ValueError, TypeError):
        return {"error": "malformed input"}, 404

    if not user:
        return {"error": "not found"}, 404
    return user.to_json(), 200

@simple_errors
def create_user():
    data = request.get_json()
    user = User(**data)
    new_user = user.save()
    nice_user = UserSchema().dump(new_user)
    return nice_user, 201

