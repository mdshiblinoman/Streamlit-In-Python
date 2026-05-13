import streamlit as st
import datetime

st.text_input('Enter your company name')
st.text_input('Enter your position')

startDate = st.date_input('Starting Date', datetime.date(2019, 7, 9))
endDate = st.date_input('Ending Date', datetime.date(2023, 5, 7))

if st.button('Date Time'):
    list = str(startDate).split('-')
    st.write(f'Start Year = {list[0]}')

