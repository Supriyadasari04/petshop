import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="🐾 Veterinary Consultation - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("🐾 Veterinary Consultation")
st.write("Book an appointment with a veterinarian.")

st.markdown("""
### Available Vets:
- Dr. Emily (Mon-Wed)
- Dr. John (Thu-Sat)

**Consultation Fee:** $40  
""")
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")