import streamlit as st

with st.container():
    st.title('This is a container')
    st.write('This is inside the container')
    st.image('image.jpg', width=200)

with st.container():
    st.write('This is another container')
    st.image('image2.jpg', width=200)   

with st.container():
    st.write('This is yet another container')
    st.image('image3.jpg', width=200)