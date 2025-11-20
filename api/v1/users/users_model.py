import datetime

import bcrypt
from mongoengine import Document, StringField, DateTimeField, ValidationError, signals


class User(Document):
    username = StringField(required=True, unique=True, min_length=3, max_length=50)
    email = StringField(required=True, unique=True)
    role = StringField(required=True, choices=["admin", "user"], default="user")
    password = StringField(required=True)
    created_at = DateTimeField(default=datetime.datetime.now(tz=datetime.timezone.utc))

    def clean(self):
        # Custom validation logic
        if "@" not in self.email:
            raise ValidationError("Invalid email address")


    @staticmethod
    def verify_credentials(username, password):
        user = User.objects(username=username).first()

        if user and bcrypt.checkpw(password.encode("utf-8"), user.password.encode("utf-8")):
            return user

        return None

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in password):
            raise ValidationError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in password):
            raise ValidationError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")

def list_all_users():
    """Return all users"""
    return User.objects()

def find_user_by_id(user_id):
    """Find a user by ID"""
    return User.objects.get(id=user_id)

# -----------------------------
# Signal handler for pre-save
# -----------------------------
def hash_password(sender, document, **kwargs):
    """
    Automatically validates and hashes the password before saving.
    Only hashes if the password is not already hashed. Checks if it starts with '$2b$' because save() runs also on updates.
    """
    if not document.password.startswith('$2b$'):
        # Validate plain-text password
        User.validate_password(document.password)
        # Hash the password
        salt = bcrypt.gensalt()
        document.password = bcrypt.hashpw(document.password.encode('utf-8'), salt).decode('utf-8')


# Connect the signal to the User model
signals.pre_save.connect(hash_password, sender=User)