import streamlit as st

st.header('Create CheckBox')

img_list = ['image.jpg', 'amazon.png']
caption_list = ['Image 1', 'Image 2']

imgs = st.checkbox('Do you want to see picture?')
if imgs:
    st.image(image=img_list, caption=caption_list, width=100)

codes = st.checkbox('Do you want to see codes?')
if codes:
    st.write('(Hello World!)')