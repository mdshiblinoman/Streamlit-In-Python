import streamlit as st

img = st.image('image.jpg', caption='This is an image')

file_name = st.text_input('Enter the Image name: ')

st.write(file_name)

with open('image.jpg', 'rb') as file:
    btn = st.download_button(
        label = 'Download Image',
        data = file,
        file_name = file_name,
        mime = 'jpg/png'
    )