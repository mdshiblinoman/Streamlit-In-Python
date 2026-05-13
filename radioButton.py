import streamlit as st

st.title('Choose Your Course')

st.radio('Choose your course',
         ['DSA', 
          'Algorithm',
          'Machine Learning',
          'Deep Learning',
          ], index= None)

