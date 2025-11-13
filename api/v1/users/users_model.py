import bcrypt
from mongoengine import Document, StringField

class User(Document):
    name = StringField(required=True)
    username = StringField(required=True)
    email = StringField(required=True)
    role = StringField(required=True)
    password = StringField(required=True)

    @staticmethod
    def create_user(user):
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(user.password.encode("utf-8"), salt)
        user = User(
            name=user.name,
            username=user.username,
            password=hashed_password.decode("utf-8"),
            email=user.email,
            role='user'
        )
        user.save()
        return user

    @staticmethod
    def verify_credentials(username, password):
        user = User.objects(username=username).first()

        if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return user

        return None



def list_all_users():
    """Return all users"""
    return User.objects()

def find_user_by_id(user_id):
    """Find a user by ID"""
    return User.objects.get(id=user_id)

