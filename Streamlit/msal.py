import streamlit as st

from msal_streamlit_authentication import msal_authentication

st.title("My Dashboard")

value = msal_authentication(
    auth={
        "clientId": "40dfba06-73cd-4de5-8b03-1fa7ca2580b7",
        "authority": "https://login.microsoftonline.com/296ca264-a31d-4ced-a5bb-cf30157d52bd",
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": ["40dfba06-73cd-4de5-8b03-1fa7ca2580b7/.default"]
    },
    key=1
)

st.write("Received", value)