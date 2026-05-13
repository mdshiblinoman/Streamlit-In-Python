import streamlit as st

fName = st.text_input('First Team Name: ')
sName = st.text_input('Second Team Name: ')

time = st.time_input('Start Time: ')

if st.button('Show'):
    st.write(f'Start the match in {fName} vs {sName} at {time}')