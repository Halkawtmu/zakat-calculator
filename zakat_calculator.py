import streamlit as st

# Function to calculate 2.5% Zakat
def calculate_zakat(amount_iqd):
    return amount_iqd * 0.025  # 2.5% of total wealth

# Streamlit UI
st.title("Zakat Calculator (IQD)")
st.write("Developed by Halkawt Muhammad")

# User input
amount = st.number_input("Enter your wealth in IQD:", min_value=0, step=100000)

# Calculate Zakat on button press
if st.button("Calculate Zakat"):
    zakat_due = calculate_zakat(amount)
    st.success(f"Your Zakat amount is: {zakat_due:,.0f} IQD")  # Format with commas
