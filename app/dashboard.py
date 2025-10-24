import streamlit as st
from datetime import date
from .db import get_tasks, insert_task, delete_task, update_task  


def show():
    if not st.session_state.get("logged_in"):
        st.error("You are not logged in.")
        st.stop()

    username = st.session_state.get("username")
    if not username:
        st.error("Session expired. Please log in again.")
        st.stop()

    st.subheader(f"📅 {username}'s Task Calendar")

    # Fetch tasks
    tasks = get_tasks(username)

    # Select date
    selected_date = st.date_input("Select a date to view tasks:", value=date.today())

    # Filter safely
    matching_tasks = [
        task for task in tasks
        if task["date"].strftime("%Y-%m-%d") == selected_date.strftime("%Y-%m-%d")
    ]

    # Display tasks
    if matching_tasks:
        st.success(f"Tasks for {selected_date.strftime('%B %d, %Y')}:")
        for task in matching_tasks:
            col1, col2, col3 = st.columns([4, 1, 1])
            with col1:
                st.markdown(f"- ✅ **{task['title']}**")
            with col2:
                if st.button("🗑️", key=f"del_{task['id']}"):
                    delete_task(task["id"])
                    st.success(f"Deleted task '{task['title']}'")
                    st.rerun()
            with col3:
                if st.button("✎", key=f"edit_{task['id']}"):
                    st.session_state.edit_task_id = task["id"]
                    st.session_state.edit_task_title = task["title"]
                    st.session_state.edit_task_date = task["date"]
    else:
        st.info(f"No tasks found for {selected_date.strftime('%B %d, %Y')}.")

    st.divider()  # 👈 moved out of else block

    # --- Add Task Form ---
    if "show_add_form" not in st.session_state:
        st.session_state.show_add_form = False

    if st.button("➕ Add Task"):
        st.session_state.show_add_form = not st.session_state.show_add_form

    if st.session_state.show_add_form:
        st.subheader("📝 Create a New Task")
        with st.form("add_task_form", clear_on_submit=True):
            task_title = st.text_input("Task Title")
            task_date = st.date_input("Task Date", value=date.today())
            submitted = st.form_submit_button("Save Task")

            if submitted:
                if not task_title.strip():
                    st.warning("⚠️ Please enter a task title before saving.")
                else:
                    insert_task(username, task_title.strip(), task_date)
                    st.success(f"✅ Task '{task_title}' added for {task_date.strftime('%B %d, %Y')}")
                    st.session_state.show_add_form = False
                    st.rerun()

    # --- Edit Task Form ---
    if "edit_task_id" in st.session_state:
        st.divider()
        st.subheader("✏️ Edit Task")

        with st.form("edit_task_form", clear_on_submit=True):
            new_title = st.text_input("Task Title", value=st.session_state.edit_task_title)
            new_date = st.date_input("Task Date", value=st.session_state.edit_task_date)
            submitted = st.form_submit_button("💾 Save Changes")

            if submitted:
                if not new_title.strip():
                    st.warning("⚠️ Please enter a task title before saving.")
                else:
                    update_task(st.session_state.edit_task_id, new_title.strip(), new_date)
                    st.success("✅ Task updated successfully!")
                    for k in ["edit_task_id", "edit_task_title", "edit_task_date"]:
                        st.session_state.pop(k, None)
                    st.rerun()

    # --- Sidebar Logout ---
    with st.sidebar:
        if st.button("Logout"):
            for k in list(st.session_state.keys()):
                del st.session_state[k]
            st.rerun()
