# importing necessary libraries
import streamlit as st

# displaying title for the media element section
st.title('I can use media element in website')

# displaying an image with caption, width of the image is set to 300 pixels
st.image('amazon.png', caption='This is an image', width=300)

# displaying an audio file with start time of 10 seconds
st.audio('audio.oga', start_time=10)

# displaying a video file with start time of 10 seconds
st.video('video.mp4', start_time=10)
