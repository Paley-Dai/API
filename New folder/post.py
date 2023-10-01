import streamlit as st


st.title("Welcome App")


name = st.text_input("Enter your name")

if st.button("Submit"):
    if name:
        st.write(f"Welcome, {name}!")
    else:
        st.warning("Please enter your name.")
