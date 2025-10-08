import streamlit as st

#dashboard page
def show():
    st.title("Dashboard")
    st.write(f"Welcome! Your user ID is: {st.session_state.user_id}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.rerun()