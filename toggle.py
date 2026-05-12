import streamlit as st

st.header('Welcome to Toggle Code!')

toggles = st.columns(3)

with toggles[0]:
    video = st.toggle('Enable Video')
if video:
    st.video('video.mp4')

with toggles[1]:
    audio = st.toggle('Enable Audio')
if audio:
    st.audio('audio.oga')
with toggles[2]:
    image = st.toggle('Enable Picture')
if image:
    st.image('image.jpg')