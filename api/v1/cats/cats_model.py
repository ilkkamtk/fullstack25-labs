from mongoengine import Document, StringField, IntField, DateTimeField
import datetime

class Cat(Document):
    name = StringField(required=True)
    weight = IntField()
    owner = StringField()
    filename = StringField()
    birthdate = DateTimeField(default=lambda: datetime.datetime.now(tz=datetime.timezone.utc))

def list_all_cats():
    """Return all cats"""
    return Cat.objects()

def find_cat_by_id(cat_id):
    """Find a cat by ID"""
    return Cat.objects.get(id=cat_id).to_json()

def add_cat(cat):
    """Add a new cat"""
    cat_name = cat.get('cat_name')
    weight = cat.get('weight')
    owner = cat.get('owner')
    filename = cat.get('filename')
    birthdate = cat.get('birthdate')

    new_cat = Cat(
        name=cat_name,
        weight=weight,
        owner=owner,
        filename=filename,
        birthdate=birthdate
    )

    new_cat.save()

    return cat
