import streamlit as st
from google.oauth2 import service_account


def load_credentials():

    private_key_id = st.secrets["firebase_private_key_id"]
    private_key = st.secrets["firebase_private_key"].replace(
        "\\n", "\n"
    )  # Needed due to Pythons ever so helpful auto-escaping
    client_email = st.secrets["firebase_client_email"]

    credentials = {
        "type": "service_account",
        "project_id": "firebase-svelte-381023",
        "private_key_id": private_key_id,
        "private_key": private_key,
        "client_email": client_email,
        "client_id": "110549956928776510458",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-8v6my%40firebase-svelte-381023.iam.gserviceaccount.com",
    }

    google_auth_credentials = service_account.Credentials.from_service_account_info(
        info=credentials
    )

    return google_auth_credentials
