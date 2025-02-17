import streamlit as st

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="🧑‍⚕️ Salon & Vet Appointments - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)


st.title("🧑‍⚕️ Salon & Vet Appointments")
st.write("Manage pet salon and vet appointment bookings.")



# Appointments overview
st.write("🔹 Upcoming Appointments:")
# Placeholder for appointment list
st.write("(Appointment schedule will be displayed here)")

st.button("✅ Confirm Selected Appointment")
st.button("🚫 Cancel Selected Appointment")


# Back to Admin Dashboard
st.page_link("pages/admin_dashboard.py", label="⬅️ Back to Admin Dashboard", icon="🏠")