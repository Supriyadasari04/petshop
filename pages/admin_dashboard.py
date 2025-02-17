import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="Admin Dashboard - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


# Function to display the Admin Dashboard
def admin_home():
    st.title("Admin Dashboard - Paws & Claws Pet Shop")
    st.write("Welcome to the Admin dashboard! Choose an option to manage the system.")
    
    # Buttons for each section with links to respective pages
    col1, col2 = st.columns(2)

    with col1:
        st.page_link("pages/manage_inventory.py", label="🛒 Manage Inventory", icon="🐾")
        st.page_link("pages/salon_vet_appointments.py", label="🧑‍⚕️ Salon & Vet Appointments", icon="🐾")
        

    with col2:
        st.page_link("pages/manage_users.py", label="👤 Manage Users", icon="🐾")
        st.page_link("pages/view_orders.py", label="📋 View Orders", icon="🐾")
    
admin_home()
st.page_link("main.py", label="⬅️ Back to Main Page", icon="🏠")
# You can call admin_home() function to run this code

