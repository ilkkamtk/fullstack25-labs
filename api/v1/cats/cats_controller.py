from flask import request
from .cats_model import list_all_cats, find_cat_by_id, add_cat
from ...utils.auth_utils import token_required


def get_cats():
    """Get all cats"""
    cats = list_all_cats()
    return cats.to_json(), 200

def get_cat_by_id(id):
    try:
        cat = find_cat_by_id(id)
    except:
        return {"error": "malformed input"}, 404

    if not cat:
        return {"error": "not found"}, 404
    return cat.to_json(), 200

@token_required
def create_cat(current_user):
    data = request.get_json()
    print('Debug', current_user.id)
    data['owner'] = str(current_user.id)
    cat = add_cat(data)

    return cat, 200
