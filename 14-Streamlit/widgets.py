import streamlit as st
import pandas as pd

st.title("Streamlit text input")

name = st.text_input("Enter your name", "Type here...")

age = st.slider("Select your age", 0, 100, 25)

st.write(f"Your age is: {age}")

options = ["Python", "Java", "C++","C", "JavaScript"]
choice = st.selectbox("Choose your favorite language:", options)
st.write(f"You selected {choice}.")


if name:
    st.write(f"Hello, {name}!")

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

df = pd.DataFrame(data)
df.to_csv("data.csv")
st.write(df)

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Data from uploaded CSV file:")
    st.write(df)