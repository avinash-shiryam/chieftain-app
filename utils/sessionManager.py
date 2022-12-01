import streamlit as st

def set_defaults():
    if "information" not in st.session_state:
        st.session_state["information"] = False
    if "authorization" not in st.session_state:
        st.session_state["authorization"] = False
    if "final" not in st.session_state:
        st.session_state["final"] = False