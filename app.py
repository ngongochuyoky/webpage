import streamlit as st

st.set_page_config(page_title="My WWebpage", page_icon=":tada:",layout="wide")

with st.container():
    st.json({
         'foo': 'bar',
         'baz': 'boz',
         'stuff': [
             'stuff 1',
             'stuff 2',
             'stuff 3',
             'stuff 5',
         ],
     })
