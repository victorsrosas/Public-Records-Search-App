import streamlit as st

st.title("Court Search App") #names of the app

keyword = st.text_input("Enter search term") #create a button for user input
if st.button("Search"):
    st.write("You searched for:", keyword)
    st.write(["Case 1", "Case 2", "Case 3"])