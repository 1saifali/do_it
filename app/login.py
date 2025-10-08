import streamlit as st
from .auth import authenticate_user

#login on streamlit
def show():
    st.title("Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if 'login_error' not in st.session_state:
        st.session_state.login_error = ""

    if st.session_state.login_error:
        st.error(st.session_state.login_error)

    if st.button("Login"):
        if not username or not password:
            st.session_state.login_error = "Please enter both fields."
        else:
            user_id = authenticate_user(username, password)
            if user_id:
                st.session_state.user_id = user_id
                st.session_state.logged_in = True
                st.success("Login successful!")
                st.rerun()  # Rerun to go to dashboard
            else:
                st.session_state.login_error = "Invalid credentials" 