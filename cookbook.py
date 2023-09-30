import streamlit as st

def run():
    st.title('Cookbook')
    st.write('This is the cookbook page.')
    if st.button("Return to Dashboard"):
        st.session_state.runpage = 'dashboard'
        st.experimental_rerun()
