import streamlit as st

st.title('Select Slider:')

size = st.slider('Choose any size', 20, 500)

st.write(size)

st.image('image.jpg', width=size, caption=size)