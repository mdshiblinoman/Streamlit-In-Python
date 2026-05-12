import streamlit as st

st.title('Choose a Car')

option = st.selectbox('Choose any one', [
    'Cycle', 'Motor Cycle', 'Bus', 'Truck', 'BMW'
])

st.write(option)