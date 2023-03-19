from src.authentication_service.db.firestore import load_db
from src.models.user import User


def get_whitelisted_users() -> dict:
    db = load_db()
    docs = db.collection("whitelist").stream()

    result = dict()
    for doc in docs:
        result.update(doc.to_dict())

    return result


def query_user(email: str) -> User:
    db = load_db()
    doc = db.collection("users").document(email).get()

    return User(**doc.to_dict())
