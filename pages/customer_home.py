import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="Customer ahaome Page - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("🐶 Welcome to Paws & Claws Pet Shop 🐱")
st.write("Choose a service to explore:")

col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/adoption_center.py", label="🦸 Pet Adoption Center", icon="🐾")
    st.page_link("pages/pet_salon.py", label="💇‍♀️ Pet Salon & Grooming", icon="✂️")
    st.page_link("pages/my_orders.py", label="📦 My Orders", icon="📋")

with col2:
    st.page_link("pages/shop.py", label="🛒 Shop (Pet Food & Accessories)", icon="🛍️")
    st.page_link("pages/vet_consultation.py", label="🐾 Veterinary Consultation", icon="⚕️")
    st.page_link("pages/profile.py", label="👤 Profile Page", icon="👥")

    
st.page_link("main.py", label="⬅️ Back to Main Page", icon="🏠")