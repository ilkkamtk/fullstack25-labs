from flask import Blueprint
from .users_controller import get_users, get_user_by_id, create_user

users_bp = Blueprint('users', __name__, url_prefix='/api/v1/users')

@users_bp.route('/', methods=['GET'])
def get_all_users():
    return get_users()

@users_bp.route('/<id>', methods=['GET'])
def get_user(id):
    return get_user_by_id(id)

@users_bp.route('/<id>', methods=['PUT'])
def put_user(id):
    return {'message': 'User item updated.'}, 200

@users_bp.route('/<id>', methods=['DELETE'])
def delete_user(id):
    return {'message': 'User item deleted.'}, 200

# @users_bp.route('/', methods=['POST'])
@users_bp.post("/")
def save_user():
    return create_user()
