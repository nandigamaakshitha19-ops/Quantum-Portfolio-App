import streamlit as st

# Title
st.title("My First Streamlit App")

# Text
st.write("Hello 👋 Welcome to Streamlit!")

# User input
name = st.text_input("Enter your name:")

if name:
    st.success(f"Hello {name}! 🎉")

# Slider
number = st.slider("Pick a number", 0, 100, 50)
st.write("You selected:", number)

# Button
if st.button("Click Me"):
    st.balloons()
