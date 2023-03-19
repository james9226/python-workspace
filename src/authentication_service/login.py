import bcrypt
from src.authentication_service.db.queries import query_user


def secure_hash(password: str) -> str:
    encoded_password = bytes(password, "utf-8")
    hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return hashed


def check_password(password: str, hashed_password: str) -> bool:
    encoded_password = bytes(password, "utf-8")
    encoded_hashed_password = bytes(hashed_password, "utf-8")
    return bcrypt.checkpw(encoded_password, encoded_hashed_password)


def authenticate_login(email: str, password: str) -> bool:

    try:
        user_data = query_user(email)
    except:
        return False

    authenticated = check_password(password, user_data.hashed_password)

    if not authenticated:
        return False

    if not user_data.is_enabled:
        return False

    return True
