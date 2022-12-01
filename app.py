import streamlit as st
from utils.streamlitViews import streamlitViews
from utils.sessionManager import set_defaults

import streamlit as st

st.set_page_config(
    page_title= "Chieftain",
)

st.markdown("""
    # Chieftain

    ### Chieftain is an authentication and authorization server

""")


# This function sets the default values for all the stages
set_defaults()

app = streamlitViews()
app.run()

