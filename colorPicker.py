import streamlit as st

st.title('Select Color:')
color = st.color_picker('Pick a color', '#00f900')

st.markdown(f'<span style="color:{color}">The selected color is: {color}</span>', unsafe_allow_html=True)

st.write(f'The selected color is: {color}')