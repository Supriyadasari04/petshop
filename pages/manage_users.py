import streamlit as st
import sqlite3

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="👤 Manage Users - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Connect to SQLite database
def get_users():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers')
    users = cursor.fetchall()
    conn.close()
    return users

# Title
st.title("👤 Manage Users")
st.write("View, edit, or delete user accounts.")

# Display User List
users = get_users()

if users:
    st.write("🔹 List of Registered Users:")
    for user in users:
        st.write(f"**{user[1]}** - {user[3]}")  # Username and Email (assuming these columns)
else:
    st.write("No users found.")

# Add New User Button
if st.button("➕ Add New User"):
    # Form to add new user
    with st.form(key='add_user_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Add User")
        
        if submit_button:
            conn = sqlite3.connect('petshop.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO customers (username, password, name, email) VALUES (?, ?, ?, ?)', 
                           (username, password, name, email))
            conn.commit()
            conn.close()
            st.success("User added successfully!")
            st.experimental_rerun()

# Back to Admin Dashboard
st.page_link("pages/admin_dashboard.py", label="⬅️ Back to Admin Dashboard", icon="🏠")
