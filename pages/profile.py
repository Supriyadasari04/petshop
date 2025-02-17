import streamlit as st
import sqlite3

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="👤 Profile Page - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Function to get customer details
def get_customer(username):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers WHERE username = ?', (username,))
    customer = cursor.fetchone()
    conn.close()
    return customer

# Title
st.title("👤 Profile Page")

# Get customer data
customer = get_customer(st.session_state.username)

if customer:
    st.write(f"**Name**: {customer[2]}")  # Name (assuming it is in the second column)
    st.write(f"**Email**: {customer[3]}")  # Email (assuming it is in the third column)
else:
    st.write("No profile data found.")

# Back to Customer Home Page
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")
