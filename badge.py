# Import streamlit library
import streamlit as st  

# Display blue badge using markdown
st.markdown(":blue-badge[Home]")  

# Display blue badge using st.badge function
st.badge("Home", color="blue")  

# Display green badge using markdown
st.markdown(":green-badge[Success]")  

# Display green badge using st.badge function
st.badge("Success", color="green")  

# Display orange warning badge
st.badge("Warning", color="orange")  

# Display red error badge
st.badge("Error", color="red")  

