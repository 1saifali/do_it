# Entry point for the app
import streamlit as st
from app import login, dashboard

def main():
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_id = None

    if st.session_state.logged_in:
        dashboard.show()
    else:
        login.show()

if __name__ == "__main__":
    main()