from google.cloud import firestore  # type : ignore
import streamlit as st
from src.authentication_service.db.firestore_config import load_credentials


@st.cache_resource(ttl=30)
def load_db() -> firestore.Client:
    db = firestore.Client(
        project="firebase-svelte-381023", credentials=load_credentials()
    )
    return db
