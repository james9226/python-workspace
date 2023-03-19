import streamlit as st
from src.authentication_service.streamlit_authenticator import Authenticate
from src.pages.uber_dashboard import build_uber_dashboard

st.set_page_config(
    page_title="Uber Dashboard",
    page_icon="🚕",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={"About": "# This is a header. This is an *extremely* cool app!"},
)

authenticator = Authenticate(
    "python-workspace-cookie", st.secrets["cookie_signing_key"], 30
)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status:
    authenticator.logout("Logout", "sidebar")
    with st.sidebar:
        st.write(f"Welcome *{name}*")
    build_uber_dashboard()
elif authentication_status is False:
    st.error("Username/password is incorrect")
elif authentication_status is None:
    st.warning("Please enter your username and password")
