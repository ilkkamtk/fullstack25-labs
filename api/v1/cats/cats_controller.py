from flask import request
from .cats_model import list_all_cats, find_cat_by_id, add_cat

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

def create_cat():
    # option 1
    data = request.get_json()
    cat = add_cat(data)

    return cat, 200

    # option 2
    #cat = add_cat(request.get_json())
    #return cat, 200

    # option 3
    #return add_cat(request.get_json()), 200
