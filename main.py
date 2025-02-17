import streamlit as st
import sqlite3

# Set Streamlit page configuration
st.set_page_config(page_title="Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Function to authenticate Admin
def authenticate_admin(admin_id, password):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM admins WHERE admin_id = ? AND password = ?', (admin_id, password))
    admin = cursor.fetchone()
    conn.close()
    return admin

# Function to authenticate Customer
def authenticate_customer(username, password):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE username = ? AND password = ?', (username, password))
    customer = cursor.fetchone()
    conn.close()
    return customer

# Function to register a new customer
def register_customer(username, password, name, email):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO customers (username, password, name, email) VALUES (?, ?, ?, ?)', 
                   (username, password, name, email))
    conn.commit()
    conn.close()

# Title
st.title("🐶 Welcome to Paws & Claws Pet Shop 🐱")
st.write("Your one-stop destination for pet adoption, food, grooming, and veterinary services.")

# Quote Section
st.markdown(
    """
    *"Animals are such agreeable friends—they ask no questions; they pass no criticisms."*  
    — George Eliot  
    """
)

st.markdown("---")

# Buttons for Login and Register
col1, col2 = st.columns(2)

with col1:
    if st.button("🔑 Login", use_container_width=True):
        st.session_state.page = "login"
        st.rerun()

with col2:
    if st.button("📝 Register", use_container_width=True):
        st.session_state.page = "register"
        st.rerun()

# Handle login
if st.session_state.get("page") == "login":
    st.header("Login Page")
    user_type = st.radio("Select user type:", ["Admin", "Customer"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if user_type == "Admin":
        admin_id = st.text_input("Admin ID")

    if st.button("Login"):
        if user_type == "Admin":
            if authenticate_admin(admin_id, password):
                st.session_state.page = "admin_dashboard"
                st.session_state.user_type = "admin"
                st.session_state.username = admin_id
                st.rerun()
            else:
                st.error("Invalid Admin credentials. Please try again.")

        elif user_type == "Customer":
            if authenticate_customer(username, password):
                st.session_state.page = "customer_home"
                st.session_state.user_type = "customer"
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid Customer credentials. Please try again.")

# Handle registration
elif st.session_state.get("page") == "register":
    st.header("Register Page")
    name = st.text_input("Name")
    email = st.text_input("Email")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        register_customer(username, password, name, email)
        st.success("Registration successful! Please login now.")
        st.session_state.page = "login"
        st.rerun()

# Redirect to respective dashboards
elif st.session_state.get("page") == "admin_dashboard":
    st.switch_page("pages/admin_dashboard.py")

elif st.session_state.get("page") == "customer_home":
    st.switch_page("pages/customer_home.py")
