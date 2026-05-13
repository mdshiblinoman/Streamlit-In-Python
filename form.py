import streamlit as st

st.title('Create a Form')

with st.form(key='my_form'):
    name = st.text_input('Enter your name')
    email = st.text_input('Enter your email')
    submit_button = st.form_submit_button(label='Submit')
    age = st.number_input('Enter your age', min_value=0, max_value=120, step=1)
    
if submit_button:
    st.write(f'Name: {name}, Email: {email}, Age: {age}')