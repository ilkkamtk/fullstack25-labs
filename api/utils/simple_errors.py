from functools import wraps
from mongoengine import ValidationError

def simple_errors(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except ValidationError as e:
            # e.to_dict() gives field-level messages
            errors = e.to_dict()  # e.g. {'__all__': 'Password is required'}
            if errors:
                errors = e.to_dict()  # dict like {'__all__': 'Invalid email', 'username': 'Field is required'}
                messages = []

                for field, msg in errors.items():
                    if field == "__all__":
                        messages.append(msg)  # document-level error
                    else:
                        messages.append(f"{msg}: {field}")  # field-level error with field name

                return {"errors": messages}, 400
            else:
                # fallback: str(e)
                msg = str(e)
            return {"error": msg}, 400
        except Exception as e:
            return {"error": str(e)}, 500
    return wrapper