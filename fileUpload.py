import streamlit as st

imageFile = st.file_uploader('Upload Images', accept_multiple_files=True)

textFile = st.file_uploader('Upload Text', accept_multiple_files=True)

if imageFile:
    for img in imageFile:
        st.write("filename", img.name)
        st.image(img)

if textFile:
    for txt in textFile:
        st.write("filename", txt.name)
        st.write(txt)