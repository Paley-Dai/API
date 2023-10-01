import streamlit as st
import json
import datetime

# Load data from the JSON file
data_file = 'data.json'
with open(data_file, 'r') as f:
    data = json.load(f)

# Function to calculate the duration and amount
def calculate_duration_and_amount(entry_time, exit_time):
    entry_time = datetime.datetime.strptime(entry_time, "%Y-%m-%d %H:%M:%S")
    exit_time = datetime.datetime.strptime(exit_time, "%Y-%m-%d %H:%M:%S")
    duration = exit_time - entry_time
    minutes = duration.total_seconds() / 60
    amount = minutes * 1  # 1 dollar per minute
    return duration, amount

# Function to create a new JSON file with plate number, duration, and amount
def create_new_json_file_with_plate_duration_amount():
    new_data = []

    entry_data = [entry for entry in data if entry.get("status") == "entry"]
    exit_data = [entry for entry in data if entry.get("status") == "exit"]

    for entry_exit_pair in zip(entry_data, exit_data):
        entry_time = entry_exit_pair[0].get("entry_time")
        exit_time = entry_exit_pair[1].get("exit_time")
        plate_number = entry_exit_pair[0].get("plate_number")

        if entry_time and exit_time and plate_number:
            duration, amount = calculate_duration_and_amount(entry_time, exit_time)
            new_data.append({
                "plate_number": plate_number,
                "duration": str(duration),
                "amount": amount
            })

    # Save the new data to a separate JSON file
    new_data_file = 'new.json'
    with open(new_data_file, 'w') as f:
        json.dump(new_data, f, indent=4)

    return new_data_file

# Streamlit app
st.title("License Plate Entry and Exit Times")

# Streamlit UI
st.subheader("Calculate Total Amount and Create New JSON File")
if st.button("Calculate Amount and Save"):
    new_data_file = create_new_json_file_with_plate_duration_amount()
    st.success(f"Data with plate, duration, and amount saved to {new_data_file}")

# Display the data
st.subheader("Original Data")
st.json(data)
