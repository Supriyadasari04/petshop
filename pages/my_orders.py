import streamlit as st
import sqlite3

# Set Streamlit page configuration and disable sidebar
st.set_page_config(page_title="📦 My Orders - Paws & Claws Pet Shop", page_icon="🐾", menu_items=None)

# Function to fetch orders for a customer
def get_customer_orders(username):
    conn = sqlite3.connect('petshop.db')
    cursor = conn.cursor()
    
    # Fetching all orders placed by the customer (including pet adoptions, purchases, and salon bookings)
    cursor.execute('''
        SELECT o.order_id, o.order_date, o.status, o.total_amount, 
               a.pet_name, a.adopted_date, s.service_name, s.booking_date
        FROM orders o
        LEFT JOIN adoptions a ON o.order_id = a.order_id
        LEFT JOIN salon_bookings s ON o.order_id = s.order_id
        WHERE o.customer_username = ?
        ORDER BY o.order_date DESC
    ''', (username,))
    
    orders = cursor.fetchall()
    conn.close()
    return orders

# Display customer orders
def display_orders(orders):
    if orders:
        for order in orders:
            order_id = order[0]
            order_date = order[1]
            status = order[2]
            total_amount = order[3]
            pet_name = order[4]
            adopted_date = order[5]
            service_name = order[6]
            booking_date = order[7]
            
            # Display order details
            st.write(f"### Order ID: {order_id}")
            st.write(f"**Order Date:** {order_date}")
            st.write(f"**Status:** {status}")
            st.write(f"**Total Amount:** ${total_amount}")
            
            if pet_name:
                st.write(f"**Adopted Pet:** {pet_name} (Adopted on {adopted_date})")
            if service_name:
                st.write(f"**Service Booked:** {service_name} (Booked on {booking_date})")
                
            st.write("---")
    else:
        st.write("No orders found.")

# Title
st.title("📦 My Orders")
st.write("Track your orders and adoptions.")

# Get orders for the logged-in customer
username = st.session_state.get("username")  # Assuming username is stored in session state
orders = get_customer_orders(username)

# Display the orders
display_orders(orders)

# Back to Customer Home Page
st.page_link("pages/customer_home.py", label="⬅️ Back to Customer Home Page", icon="🏠")
