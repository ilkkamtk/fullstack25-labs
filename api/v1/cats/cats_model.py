# Mock data
cat_items = [
    {
        'cat_id': 9592,
        'cat_name': 'Frank',
        'weight': 11,
        'owner': 3609,
        'filename': 'f3dbafakjsdfhg4',
        'birthdate': '2021-10-12',
    },
    {
        'cat_id': 9590,
        'cat_name': 'Mittens',
        'weight': 8,
        'owner': 3602,
        'filename': 'f3dasdfkjsdfhgasdf',
        'birthdate': '2021-10-12',
    },
]

def list_all_cats():
    """Return all cats"""
    return cat_items

def find_cat_by_id(cat_id):
    """Find a cat by ID"""

    for cat in cat_items:
        if cat['cat_id'] == int(cat_id):
            return cat
    return None


    # this line is same as the one above
    #return next((cat for cat in cat_items if cat['cat_id'] == int(cat_id)), None)

def add_cat(cat):
    """Add a new cat"""
    cat_name = cat.get('cat_name')
    weight = cat.get('weight')
    owner = cat.get('owner')
    filename = cat.get('filename')
    birthdate = cat.get('birthdate')

    new_id = cat_items[0]['cat_id'] + 1
    new_cat = {
        'cat_id': new_id,
        'cat_name': cat_name,
        'weight': weight,
        'owner': owner,
        'filename': filename,
        'birthdate': birthdate
    }
    cat_items.insert(0, new_cat)
    return {'cat_id': new_id}
