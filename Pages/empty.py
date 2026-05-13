import streamlit as st
import time

time = st.time_input('Select Time:')
if st.button('Show'):
    for seconds in range(int(time)):
        st.write(f'{seconds} seconds have passed')
        time.sleep(1)