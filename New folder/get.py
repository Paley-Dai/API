import streamlit as st
import requests

API_URL = "https://hotelyesapi.vercel.app/menu/getAllMenu"

def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 201:
        data = response.json()
        return data
    else:
        st.error(f"Error fetching data. Status code: {response.status_code}")
        return None

def main():
    st.title("Data from hotelyesapi")

    data = fetch_data()

    if data:
        st.table(data)

if __name__ == "__main__":
    main()
