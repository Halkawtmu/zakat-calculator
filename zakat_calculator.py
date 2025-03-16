import streamlit as st

def calculate_zakat(amount_iqd):
    return (amount_iqd // 1000000) * 25000

st.title("Zakat Calculator (IQD)")
st.write("Developed by Halkawt Muhmmed")

amount = st.number_input("Enter your wealth in IQD:", min_value=0, step=100000)
if st.button("Calculate Zakat"):
    zakat_due = calculate_zakat(amount)
    st.success(f"Your Zakat amount is: {zakat_due} IQD")