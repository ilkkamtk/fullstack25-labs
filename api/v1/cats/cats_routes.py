from flask import Blueprint
from .cats_controller import get_cats

cats_bp = Blueprint('cats', __name__, url_prefix='/api/v1/cats')

@cats_bp.route('/', methods=['GET'])
def get_all_cats():
    return get_cats()