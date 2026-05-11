# importing necessary libraries
import streamlit as st

# displaying an image with caption
img = st.image('image.jpg', caption='This is an image')

# input field to get the name of the file to be downloaded
file_name = st.text_input('Enter the Image name: ')

# displaying the name of the file to be downloaded
st.write(file_name)

# creating a download button to download the image
with open('image.jpg', 'rb') as file:
    btn = st.download_button(
        label = 'Download Image',   # label for the download button
        data = file,                # data to be downloaded
        file_name = file_name,      # name of the file to be downloaded
        mime = 'jpg/png'            # MIME type of the file to be downloaded
    )

