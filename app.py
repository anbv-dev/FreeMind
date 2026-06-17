import streamlit as st
from decision_engine import get_response

st.title("FreeMind")
st.write("AI App that helps you make complex decisions with ease")

st.divider()

user_input = st.text_input("Ask anything that's troubling you...")

if st.button("Ask"):
    print("check")
    st.code(get_response(user_input))
