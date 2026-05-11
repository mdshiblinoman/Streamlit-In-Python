import streamlit as st  # Import streamlit library

st.markdown(":blue-badge[Home]")  # Display blue badge using markdown
st.badge("Home", color="blue")  # Display blue badge using st.badge function
st.markdown(":green-badge[Success]")  # Display green badge using markdown
st.badge("Success", color="green")  # Display green badge using st.badge function

st.badge("Warning", color="orange")  # Display orange warning badge
st.badge("Error", color="red")  # Display red error badge