import streamlit as st

def run():
    st.title('Cookbook')
    if st.button("Return to Dashboard"):
        st.session_state.runpage = 'dashboard'
        st.experimental_rerun()
    st.write('## What is your data set?')
    st.write('Evolution of Intel CPUs')
    st.write('## Where did you acquire your data set?')
    st.write('From Kaggle by Luca Ortolan')
    st.write('## Why did you choose this data set?')
    st.write('answer')
    st.write('## Steps on how we processed the Dataset. (Cleaning, Filtering, Etc.)')
    st.write('answer')
    
