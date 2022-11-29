import streamlit as st

from utils import chieftain_req

st.set_page_config(
    page_title= "Login Page",
)

st.title("Login")


def display(status="not_logged_in"):

    placeholder = st.empty()

    if status == "not_logged_in":

        with placeholder.container():
            with st.form(key="not_logged_in"):
                email_ophone = st.text_input("Enter email or phone number")
                submit = st.form_submit_button("Submit")
                init_output = (chieftain_req.authenticate(email_ophone=email_ophone))
                print(init_output)
        try:
            if init_output["challenge_id"]:
                placeholder.empty()
                display(status="otp_sent")
            else:
                display()
        except:
            pass

    elif status == "otp_sent":

        with placeholder.container():
            with st.form(key="otp_sent"):

                otp = st.text_input("Enter the OTP")
                challenge_id = st.text_input("Enter the challenge_id")
                submit = st.form_submit_button("Submit")
                init_output = (chieftain_req.answer(otp=otp,challenge_id=challenge_id,email_ophone=email_ophone))
                print(init_output)
        try:
            if init_output["auth_token"] :
                placeholder.empty()
                display(status="otp_entered")
            else:
                display("otp_sent")
                print("stuck here")
        except:
            pass
    
    elif status == "otp_entered":
        with placeholder.container():

                st.write("OTP entered")


display()

