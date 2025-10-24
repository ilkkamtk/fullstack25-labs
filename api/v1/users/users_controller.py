from flask import request
from .users_model import list_all_users, find_user_by_id, add_user

def get_users():
    """Get all users"""
    users = list_all_users()
    return users, 200

def get_user_by_id(id):
    try:
        user = find_user_by_id(id)
    except:
        return {"error": "malformed input"}, 404

    if not user:
        return {"error": "not found"}, 404
    return user, 200

def create_user():
    # option 1
    data = request.get_json()
    user = add_user(data)

    return user, 200

    # option 2
    #user = add_user(request.get_json())
    #return user, 200

    # option 3
    #return add_user(request.get_json()), 200
