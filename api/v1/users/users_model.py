# Mock data
user_items = [
   {
     'user_id': 3609,
     'name': 'John Doe',
     'username': 'johndoe',
     'email': 'john@metropolia.fi',
     'role': 'user',
     'password': 'password',  # Note: Never store plain text passwords in production!
  },
]

def list_all_users():
    """Return all users"""
    return user_items

def find_user_by_id(user_id):
    """Find a user by ID"""

    for user in user_items:
        if user['user_id'] == int(user_id):
            return user
    return None


    # this line is same as the one above
    #return next((user for user in user_items if user['user_id'] == int(user_id)), None)

def add_user(user):
    """Add a new user"""

    name = user.get('name')
    username = user.get('username')
    email = user.get('email')
    role = user.get('role')
    password = user.get('password')

    new_id = user_items[0]['user_id'] + 1
    new_user = {
        'user_id': new_id,
        'name': name,
        'username': username,
        'email': email,
        'role': role,
        'password': password
    }
    user_items.insert(0, new_user)
    return {'user_id': new_id}
