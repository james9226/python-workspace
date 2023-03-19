import bcrypt
from src.authentication_service.db.queries import (
    query_user,
    query_number_request_attempts,
    update_request_attempts,
)


def secure_hash(password: str) -> bytes:
    encoded_password = bytes(password, "utf-8")
    hashed = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return hashed


def check_password(password: str, hashed_password: str) -> bool:
    encoded_password = bytes(password, "utf-8")
    encoded_hashed_password = bytes(hashed_password, "utf-8")
    return bcrypt.checkpw(encoded_password, encoded_hashed_password)


def authenticate_login(email: str, password: str) -> bool:

    if query_number_request_attempts() > 1000:
        return False

    try:
        user_data = query_user(email)
    except:
        update_request_attempts(email, False, "EMAIL_NOT_FOUND_IN_DB")
        return False

    authenticated = check_password(password, user_data.hashed_password)

    if not authenticated:
        update_request_attempts(email, False, "FAILED_PASSWORD_AUTHENTICATION")
        return False

    if not user_data.is_enabled:
        update_request_attempts(email, False, "USER_IS_DISABLED")
        return False

    update_request_attempts(email, True, "USER_ENABLED_AND_PASSWORD_AUTHENTICATED")
    return True
