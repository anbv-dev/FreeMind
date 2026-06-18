import streamlit as st
from decision_engine import get_response

st.set_page_config(page_title="FreeMind", page_icon="./source/favicon.ico")

st.title("Free:red[Mind]")
st.write("_AI App that helps you make complex decisions with ease_")

st.divider()

with st.form(key="prompt_window"):

    user_input = st.text_input("Ask anything that's troubling you...")

    if st.form_submit_button("Ask"):
        print("button pressed")
        with st.spinner("Finding the optimal solution to your issue..."):
            st.write(get_response(user_input))
