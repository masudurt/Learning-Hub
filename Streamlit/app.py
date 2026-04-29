#In the terminal type 
#      >> streamlit run app.py
#       This executes the file named "app.py" as webapp in the browser.
#Click on ctrl and point and click mouse to the given link to visit the webapp in the browser.
#To terminate the terminal press ctrl and c on the keyboard.
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

import streamlit as st
import pandas as pd
import numpy as np
#Display a title
st.title("This is a title from streamlit has been used.")

#Display a text
st.write("Hellow Bhai")

#Create a dataframe and display
df = pd.DataFrame({
    'First Column': [1, 2, 3],
    'Second Column': [4, 5, 6]
})
st.write(df)

#Show dataframe as tabular and then line chart format
chart_data = pd.DataFrame(
    np.random.randn(20,3),  # 20 rows and 3 columns
    columns=['a','b','c']
)
st.write(chart_data) #tabular
st.line_chart(chart_data) #Line chart

#Take name as input and display 
name = st.text_input("Enter your name")
if name == "Tawhid":
    st.write(f"Sir! Good Morning!")
elif name:
    st.write(f"Hello {name}! How's it going?")

#Take age as input - slider
age = st.slider("Provide your actual age.",0,100,25) #0-100 with 25 as default
if age<18:
    st.write(f"Hey kid! As you are {age} years old, you can play inside that park.")
elif age<38:
    st.write(f"Hey young man! Your age {age} is great! Let's have a party! Shall we?")
elif age>38:
    st.write(f"Hellow Sir! How can we help you?")
else:
    st.write(f"Hope you are fine!")
    
#Options
options = ["Option 1", "Option 2", "Option 3"]
choice = st.selectbox("Select an option", options)
st.write(f"You selected: {choice}")

#Upload a csv file and display
uploaded_file = st.file_uploader("Upload your CSV file", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    