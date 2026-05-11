# importing necessary libraries
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# create a sample dataframe with random data
df = pd.DataFrame(
    rng(0).standard_normal((50, 20)), columns=("col %d" % i for i in range(20))
)

# displaying dataframe with interactive features
st.dataframe(df)