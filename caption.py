# Streamlit caption example
import streamlit as st

# Display a simple caption
st.caption("This is a caption")

# Display a caption with markdown and emoji
body = "This is a caption with **markdown** and :smile: emoji"

# Display the caption with HTML allowed
st.caption(body, unsafe_allow_html=False, help=None, width="stretch", text_alignment="left")

