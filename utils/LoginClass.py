import requests
from utils import chieftain_req


class LoginClass():

    def __init__(self,email_ophone=None,challenge_id=None,otp=None,auth_token=None):
        self.email_ophone = email_ophone
        self.challenge_id = challenge_id
        self.otp = otp
        self.auth_token = auth_token
    
    def authenticate(self):
        
        response = chieftain_req.authenticate(email_ophone=self.email_ophone)
        print(response)

    def answer(self):
        
        response = chieftain_req.answer(email_ophone=self.email_ophone,
                                        otp=self.otp,
                                        challenge_id=self.challenge_id)
        
        print(response)

    def authorize(self):
        
        response = chieftain_req.authorize(auth_token=self.auth_token)
        print(response)

    def logout(self):
        
        response = chieftain_req.authorize(auth_token=self.auth_token)
        print(response)

loginInstance = LoginClass(email_ophone="avinash.reddy@shiryam.com",otp=217642,challenge_id=667)

loginInstance.answer()