import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="💇‍♀️ Pet Salon & Grooming - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("💇‍♀️ Pet Salon & Grooming")
st.write("Book a grooming session for your pet.")

st.markdown("""
### Services Available:
- Bath & Blow Dry - $25
- Nail Trimming - $15
- Full Grooming - $50
""")
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")