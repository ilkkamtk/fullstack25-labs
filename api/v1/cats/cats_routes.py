from flask import Blueprint
from .cats_controller import get_cats, get_cat_by_id, create_cat

cats_bp = Blueprint('cats', __name__, url_prefix='/api/v1/cats')

@cats_bp.route('/', methods=['GET'])
def get_all_cats():
    return get_cats()

@cats_bp.route('/<id>', methods=['GET'])
def get_cat(id):
    return get_cat_by_id(id)

@cats_bp.route('/<id>', methods=['PUT'])
def put_cat(id):
    return {'message': 'Cat item updated.'}, 200

@cats_bp.route('/<id>', methods=['DELETE'])
def delete_cat(id):
    return {'message': 'Cat item deleted.'}, 200

# @cats_bp.route('/', methods=['POST'])
@cats_bp.post("/")
def save_cat():
    return create_cat()
