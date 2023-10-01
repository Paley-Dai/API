import streamlit as st
import requests

# Streamlit app
st.title("Display JSON Data in a Table")

# Function to fetch JSON data from the Flask API
def fetch_data():
    try:
        response = requests.get("http://localhost:5000/get_data")  # Replace with the actual API URL
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            st.error(f"Error: {response.status_code}")
    except Exception as e:
        st.error(f"Error: {str(e)}")

# Streamlit UI
st.subheader("JSON Data in Table")

data = fetch_data()
if data:
    st.table(data)
