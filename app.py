import streamlit as st

st.title("Odd or Even Checker")

number = st.number_input("Enter a number", step=1, value=0)

if st.button("Check"):
    if number % 2 == 0:
        st.success(f"{int(number)} is even")
    else:
        st.success(f"{int(number)} is odd")
