import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# App Configuration
st.set_page_config(page_title="Bible Study Planner", page_icon="📖")

st.title("📖 Weekly Bible Study Poll")
st.write("Enter your name and pick the days that work best for your schedule!")

# Create a connection to Google Sheets
conn = st.connection("gsheets", type=GSheetsConnection)

# 1. User Input Form
with st.form("poll_form"):
    name = st.text_input("Your Name")
    
    st.write("### Which days work for you?")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    # Create a dictionary of checkboxes
    selections = {day: st.checkbox(day) for day in days}
    
    notes = st.text_area("Any specific time preferences?")
    
    submit = st.form_submit_button("Submit Availability")

# 2. Data Handling Logic
if submit:
    if name:
        # Prepare the new row of data
        selected_days = [day for day, checked in selections.items() if checked]
        new_row = pd.DataFrame([{
            "Name": name,
            "Days": ", ".join(selected_days),
            "Notes": notes
        }])

        # Fetch existing data, add new row, and update the sheet
        existing_data = conn.read(worksheet="Sheet1")
        updated_df = pd.concat([existing_data, new_row], ignore_index=True)
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.success(f"Thanks {name}! Your preferences are saved.")
        st.balloons()
    else:
        st.warning("Please enter your name.")

# 3. View Current Results (Optional)
if st.checkbox("Show who has responded so far"):
    current_responses = conn.read(worksheet="Sheet1")
    st.dataframe(current_responses)
    
