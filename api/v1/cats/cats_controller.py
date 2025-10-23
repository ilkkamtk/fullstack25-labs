from .cats_model import list_all_cats

def get_cats():
    """Get all cats"""
    cats = list_all_cats()
    return cats, 200