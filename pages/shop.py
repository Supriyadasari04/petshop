import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="🛒 Pet Shop - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Title
st.title("🛒 Pet Shop")
st.write("Browse our pet food and accessories.")

# Example products
products = [
    {"name": "Premium Dog Food", "price": 20},
    {"name": "Cat Tuna Treats", "price": 15},
    {"name": "Cozy Pet Bed", "price": 30},
]

# Display products
for product in products:
    if st.button(f"Add {product['name']} to Cart - ${product['price']}"):
        # Add product to session cart
        if "cart" not in st.session_state:
            st.session_state.cart = []
        st.session_state.cart.append(product)
        st.success(f"Added {product['name']} to your cart.")

# Display shopping cart
if "cart" in st.session_state and st.session_state.cart:
    st.write("🛒 Your Cart:")
    total = 0
    for item in st.session_state.cart:
        st.write(f"{item['name']} - ${item['price']}")
        total += item['price']
    st.write(f"**Total**: ${total}")

# Back to Customer Home Page
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")
