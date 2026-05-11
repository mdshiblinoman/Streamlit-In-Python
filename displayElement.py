# importing necessary libraries
import streamlit as st
import pandas as pd

st.metric(label="Temperature", value="70 °F", delta="1.2 °F")  # Display metric with label, value, and delta

st.metric(label="Temperature", value="70 °F", delta="1.2 °F", delta_color="inverse")  # Display metric with inverse delta color

table = ({
    "Name": ["John", "Jane", "Jack"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
})

st.table(table)  # Display table using st.table function

st.dataframe(table)  # Display table using st.dataframe function with interactive features