# importing necessary libraries
import streamlit as st

# creat header for the app
st.header('Link Button Example')

# create a list of image and caption
image_list = ['image.jpg', 'amazon.png']
caption_list = ['Image 1', 'Image 2']

# show the image into side by side
st.image(image=image_list, width=100, caption=caption_list)

# create a link button
st.link_button('Click here to visit youtube', 'https://www.youtube.com/watch?v=FEKX1FjLAlo&list=PLMi6KgK4_mk2rK5jD-BK5RigFIP2QSq8W&index=7')