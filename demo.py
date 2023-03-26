from datetime import datetime
import streamlit as st
from src.authentication_service.streamlit_authenticator import Authenticate
from src.pages.uber_dashboard import build_uber_dashboard

# This is a hack to prevent state variables become descoped and temporarily deleted.
# This whole streamlit_authenticator package needs a rewrite to properly handle this bug
# as it does not currently handle the state in the correct way!

st.set_page_config(
    page_title="Uber Dashboard",
    page_icon="🚕",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items={"About": "# This is a header. This is an *extremely* cool app!"},
)

authenticator = Authenticate(
    "python-workspace-cookie", st.secrets["cookie_signing_key"], 30
)

# name, authentication_status, username, login_failure = authenticator.login(
#     "Login", "main"
# )

name, authentication_status, username = authenticator.login("Login", "main")

print(datetime.now(), authentication_status)

if authentication_status:
    with st.sidebar:
        st.title("Python Workspace Demo Dashboard")
    authenticator.logout("Logout", "sidebar")
    with st.sidebar:
        st.write(f"Welcome *{name}*")
    build_uber_dashboard()
# elif authentication_status is False and login_failure is True:
#     st.error("Username/password is incorrect")
elif authentication_status is False:
    authenticator.login_component("Login")
    st.error("Username/password is incorrect")
elif authentication_status is None:
    authenticator.login_component("Login")
    st.warning("Please enter your username and password")
else:
    st.spinner()
