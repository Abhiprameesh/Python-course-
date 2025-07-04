import streamlit as st
import pandas as pd
import numpy as np

## Title of the aplication
st.title("Hello streamlit application")

st.write("This is a simple streamlit app i created ")

df = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

st.write("Below is a dataframe:")
st.write(df)


chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)
st.line_chart(chart_data)