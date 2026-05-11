import streamlit as st

st.caption("This is a caption")

body = "This is a caption with **markdown** and :smile: emoji"
st.caption(body, unsafe_allow_html=False, help=None, width="stretch", text_alignment="left")