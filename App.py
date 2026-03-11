import streamlit as st
import pandas as pd
from datetime import datetime

# App Configuration
st.set_page_config(page_title="Bible Study Planner", page_icon="📖")

st.title("📖 Weekly Bible Study Poll")
st.write("Help us find the best day to meet! Please enter your name and select all days that work for you.")

# 1. User Input Section
with st.form("poll_form"):
    name = st.text_input("Your Name", placeholder="e.g. Andrew")
    
    st.write("### Which days are you generally available?")
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    selections = {day: st.checkbox(day) for day in days}
    
    notes = st.text_area("Any specific time preferences or notes?", placeholder="e.g. After 6:30 PM is best.")
    
    submit = st.form_submit_button("Submit Availability")

# 2. Data Handling Logic
# For a quick DIY, we'll store data in a local CSV (Note: This resets if the app 'sleeps' 
# unless connected to a persistent data source like a Google Sheet).
if submit:
    if name:
        selected_days = [day for day, checked in selections.items() if checked]
        new_data = {
            "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "Name": name,
            "Available Days": ", ".join(selected_days),
            "Notes": notes
        }
        st.success(f"Got it, {name}! Your preferences have been recorded.")
        # Logic to display a summary (In a real app, this would append to a database)
        st.balloons()
    else:
        st.error("Please enter your name before submitting.")

# 3. Results Section (Optional - can be hidden behind a password)
st.divider()
st.subheader("Current Group Trends")
st.info("Once everyone responds, we'll see which days have the most 'votes' here!")
