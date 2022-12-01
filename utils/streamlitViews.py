import streamlit as st
from utils.LoginClass import LoginClass

# Session state initializer

def information_state():
        st.session_state["information"] = True
def authorization_state():
        st.session_state["authorization"] = True
def final_state():
        st.session_state["final"] = True

#TODO (avinash) : need to assign variable names to each text input channel and send it to LoginClass

class streamlitViews():

    def __init__(self,view_type=None):
        self.view_type = view_type
        self.placeholder = st.empty()

    def view_handler(self):
        if self.view_type == "information_stage":
            self.information_stage()
        elif self.view_type == "authorization_stage":
            self.authorization_stage()
        elif self.view_type == "final_stage":
            self.final_stage()

    def information_stage(self):

        with self.placeholder.container():
            st.text_input("Enter your email id or phone number")
            submit_button = st.button("Submit",key = "information_submit", on_click=information_state)


            if submit_button or st.session_state['information']:
                self.placeholder.empty()
                self.authorization_stage()

    def authorization_stage(self):


        with self.placeholder.container():
            st.text_input("Enter OTP")
            st.text_input("Enter challenge id ")
            submit_button = st.button("Submit OTP", key = "authorization submit", on_click=authorization_state)


            if submit_button or st.session_state['authorization']:
                self.placeholder.empty()
                self.final_stage()
    
    def final_stage(self):

        with self.placeholder.container():
            self.placeholder.empty()
            st.sidebar.success("Logged in successfully")     
    
    def run(self):
        self.information_stage()


