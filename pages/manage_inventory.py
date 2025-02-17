import streamlit as st
import sqlite3

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="🛒 Manage Inventory - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Connect to SQLite database
def get_inventory():
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM inventory')
    inventory = cursor.fetchall()
    conn.close()
    return inventory

# Title
st.title("🛒 Manage Inventory")
st.write("Add, update, or remove products.")

# Display Inventory
inventory = get_inventory()

if inventory:
    st.write("🔹 Inventory Overview:")
    for item in inventory:
        st.write(f"**{item[1]}** - {item[2]} - ${item[3]}")  # Name, Description, Price (assumes these columns exist)
else:
    st.write("No inventory items found.")

# Add New Item Button
if st.button("➕ Add New Item"):
    # Form to add new item
    with st.form(key='add_item_form'):
        name = st.text_input("Item Name")
        description = st.text_area("Description")
        price = st.number_input("Price", min_value=0.0, format="%.2f")
        submit_button = st.form_submit_button("Add Item")
        
        if submit_button:
            conn = sqlite3.connect('petshop.db')
            cursor = conn.cursor()
            cursor.execute('INSERT INTO inventory (name, description, price) VALUES (?, ?, ?)', 
                           (name, description, price))
            conn.commit()
            conn.close()
            st.success("Item added successfully!")
            st.experimental_rerun()

# Back to Admin Dashboard
st.page_link("pages/admin_dashboard.py", label="⬅️ Back to Admin Dashboard", icon="🏠")
