import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="📋 View Orders - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("📋 View Orders")
st.write("Review and manage customer orders.")



# Orders overview
st.write("🔹 List of pending & completed orders:")
# Placeholder for order table
st.write("(Order data table will be displayed here)")

st.button("✅ Approve Selected Order")
st.button("🚫 Cancel Selected Order")


# Back to Admin Dashboard
st.page_link("pages/admin_dashboard.py", label="⬅️ Back to Admin Dashboard", icon="🏠")