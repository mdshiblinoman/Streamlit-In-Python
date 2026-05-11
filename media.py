import streamlit as st

st.title('I can use media element in website')

st.image('amazon.png', caption='This is an image', width=300)

st.audio('audio.oga', start_time=10)

st.video('video.mp4', start_time=10)