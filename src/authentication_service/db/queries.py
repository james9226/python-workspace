import datetime
from src.authentication_service.db.firestore import load_db
from src.models.user import User
import streamlit as st


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


@st.cache_data(ttl=60, show_spinner=False)
def query_number_request_attempts() -> int:
    db = load_db()
    collection = (
        db.collection("login_request_attempts")
        .document(datetime.datetime.now().strftime("%Y-%m-%d"))
        .collection("requests")
    )
    snapshot = collection.count().get()[0]

    return snapshot[0].value


def update_request_attempts(email: str, success: bool, reason: str = ""):
    db = load_db()
    collection = (
        db.collection("login_request_attempts")
        .document(datetime.datetime.now().strftime("%Y-%m-%d"))
        .collection("requests")
    )
    collection.document().set(
        {
            "email": email,
            "event_time": datetime.datetime.now(),
            "login_successful": success,
            "reason": reason,
        }
    )
