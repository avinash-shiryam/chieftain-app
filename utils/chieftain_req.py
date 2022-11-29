import requests
import json
import re

MAIN_URL = "http://127.0.0.1:8000/"

def authenticate(**kwargs):
    URL = "http://127.0.0.1:8000/authenticate"

    email_ophone = kwargs.get("email_ophone")
    phone_number_validator = "^\\+?[1-9][0-9]{7,14}$"
    
    
    if re.match(phone_number_validator,email_ophone):
        body = {"phone_number" : email_ophone}
    else:
        body = {"email" : email_ophone}
    
    output_body = requests.post(url=URL, data = json.dumps(body))

    return output_body.json()

def answer(**kwargs):
    URL = "http://127.0.0.1:8000/answer"

    email_ophone = kwargs.get("email_ophone")
    otp = kwargs.get("otp")
    challenge_id= kwargs.get("challenge_id")

    body = {
        "challenge_id": challenge_id,
        "email" : email_ophone,
        "answer" : {
            "otp" : otp
            }
        }
    output_body = requests.post(url=URL, data = json.dumps(body))
    print(output_body.json())

    return output_body.json()



def authorize(**kwargs):
    URL = "http://127.0.0.1:8000/authorize"

def logout(**kwargs):
    URL = "http://127.0.0.1:8000/logout"
