import streamlit as st

def run():
    st.title('Cookbook')
    if st.button("Return to Dashboard"):
        st.session_state.runpage = 'dashboard'
        st.experimental_rerun()
    st.write('## What is your data set?')
    st.write('Our data set is the evolution of Intel CPUs')
    st.write('## Where did you acquire your data set?')
    st.write('We acquired it online via kaggle')
