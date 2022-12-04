import requests
import streamlit as st
from utils import chieftain_req


class LoginClass():

    def __init__(self,email_ophone=None,challenge_id=None,otp=None,auth_token=None):
        self.email_ophone = email_ophone
        self.challenge_id = challenge_id
        self.otp = otp
        self.auth_token = auth_token
    
    def authenticate(self):
        
        response = chieftain_req.authenticate(email_ophone=self.email_ophone)

        if "challenge_id" in response.keys():
            print(response)
            return response
        else:
            self.authenticate()

    def answer(self):
        
        response = chieftain_req.answer(email_ophone=self.email_ophone,
                                        otp=self.otp,
                                        challenge_id=self.challenge_id)
        
        if "auth_token" in response.keys():
            print(response)
            st.session_state['auth_token'] = response.get('auth_token')
            return response
        else:
            self.answer()
        
        print(response)

    def authorize(self):
        
        response = chieftain_req.authorize(auth_token=self.auth_token)
        print(response)

        if "is_authorised" in response.keys():
            print(response)
            return response
        else:
            self.authorize()

    def logout(self):
        
        response = chieftain_req.authorize(auth_token=self.auth_token)
        print(response)