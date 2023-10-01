import streamlit as st
import requests
import json

# Streamlit app
st.title("Send POST Request to API")

# Function to send POST request
def send_post_request(data):
    api_url = "http://localhost:5000/receive_data"
    headers = {"Content-Type": "application/json"}
    response = requests.post(api_url, data=json.dumps(data), headers=headers)
    return response

# Streamlit UI
st.subheader("Send Data to API")

# Example data in the specified format
example_data = [
    {
        "plate_number": "ABC123",
        "duration": "1:30:00",
        "amount": 90.0
    }
]

st.json(example_data)

if st.button("Send POST Request"):
    response = send_post_request(example_data)
    if response.status_code == 200:
        st.success("Data sent successfully.")
    else:
        st.error("Error sending data.")
