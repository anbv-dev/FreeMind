import streamlit as st
from decision_engine import get_response, model

# Page title and favicon
st.set_page_config(page_title="FreeMind", page_icon="./source/favicon.ico")

# UI:
st.title("Free:red[Mind]")
st.write("_AI App that helps you make complex decisions with ease_")

st.divider()

with st.form(key="prompt_window"):

    user_input = st.text_input("Ask anything that's troubling you...")
    st.caption(f"Model: {model}")

    if st.form_submit_button("Ask"):

        with st.spinner("Finding the optimal solution to your issue..."):
            response = get_response(user_input)
            st.write("Here's an analysis to your issue:")

            # UI for displaying response results
            with st.expander(label="Pros"):
                for line in response['pros']:
                    st.write(line)

            with st.expander(label="Cons"):
                for line in response['cons']:
                    st.write(line)

            with st.expander(label="Blind Spot"):
                st.write(response['blind_spot'])

            with st.expander(label="Advice"):
                st.write(response['advice'])
