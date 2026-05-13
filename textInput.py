import streamlit as st

st.title('User Input Text:')

name = st.text_input("What is your name?")
sure = st.text_input("What is your sureName?")

button = st.button('Show')

if button:
    st.write(f'Welcome {name} {sure}')