from mongoengine import Document, StringField

class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    role = StringField(required=True)
    password = StringField(required=True)

def list_all_users():
    """Return all users"""
    return User.objects()

def find_user_by_id(user_id):
    """Find a user by ID"""
    return User.objects.get(id=user_id)

def add_user(user):
    """Add a new user"""

    name = user.get('name')
    username = user.get('username')
    email = user.get('email')
    role = user.get('role')
    password = user.get('password')

    new_user = User(
        name=name,
        username=username,
        email=email,
        role=role,
        password=password
    )

    new_user.save()

    return user
