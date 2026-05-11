import streamlit as st  # Import streamlit library

st.markdown("# This is a markdown")  # Display markdown heading level 1
st.markdown("## This is a markdown")  # Display markdown heading level 2
st.markdown("### This is a markdown")  # Display markdown heading level 3

st.markdown("**This is a markdown**")  # Display bold markdown text
st.markdown("*This is a markdown*")  # Display italic markdown text
st.markdown("~~This is a markdown~~")  # Display strikethrough markdown text
st.markdown("> This is a markdown")  # Display blockquote markdown text
st.markdown("- This is a markdown")  # Display bullet point markdown
st.markdown("1. This is a markdown \n 2. This is a markdown")  # Display numbered list markdown
st.markdown("[This is a markdown](https://www.google.com)")  # Display markdown hyperlink

table = '''
| Name | Age | City |
| --- | --- | --- |
| John | 25 | New York |
| Jane | 30 | London |
| Jack | 35 | Paris |'''
st.markdown(table)  # Display markdown table

json = {
    "name": "John",
    "age": 25,
    "city": "New York"
}
st.markdown(f"```json\n{json}\n```")  # Display markdown formatted JSON data

st.markdown("This is a Funny :smile:")  # Display markdown with emoji