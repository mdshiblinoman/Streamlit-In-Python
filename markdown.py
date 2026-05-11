# Import streamlit library
import streamlit as st

# Display markdown heading level 1
st.markdown("# This is a markdown")

# Display markdown heading level 2
st.markdown("## This is a markdown")

# Display markdown heading level 3
st.markdown("### This is a markdown")

# Display bold markdown text
st.markdown("**This is a markdown**")

# Display italic markdown text
st.markdown("*This is a markdown*") 

# Display strikethrough markdown text
st.markdown("~~This is a markdown~~")

# Display blockquote markdown text
st.markdown("> This is a markdown")

# Display bullet point markdown
st.markdown("- This is a markdown")

# Display numbered list markdown
st.markdown("1. This is a markdown \n 2. This is a markdown")

# Display markdown hyperlink
st.markdown("[This is a markdown](https://www.google.com)")

# Create a table
table = '''
| Name | Age | City |
| --- | --- | --- |
| John | 25 | New York |
| Jane | 30 | London |
| Jack | 35 | Paris |'''

# Display markdown table
st.markdown(table) 

json = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

# Display markdown formatted JSON data
st.markdown(f"```json\n{json}\n```") 

# Display markdown with emoji
st.markdown("This is a Funny :smile:")  