import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="Pet Adoption Center - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("🦸 Pet Adoption Center")
st.write("Find your perfect pet companion!")

# Example pet listings
st.markdown("""
### 🐶 Max - Golden Retriever  
- Age: 2 years  
- Vaccinated: ✅ Yes  
- Adoption Fee: $200  

### 🐱 Whiskers - Persian Cat  
- Age: 3 years  
- Vaccinated: ✅ Yes  
- Adoption Fee: $150  
""")
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")