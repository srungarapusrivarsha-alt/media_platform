import streamlit as st 
# from db_c import conn,cursor
st.title("Media Platform")

login,signup = st.tabs(["Login","SignUp"])
with login:
    st.header("login_form")
    with st.form("login"):
        email=st.text_input("enter email ")
        password=st.text_input("enter password",type="password")
        button=st.form_submit_button("login")
with signup:
    st.header("signup_form")
    with st.form("signup"): 
        name=st.text_input("enter name")
        email=st.text_input("enter email")
        password=st.text_input("enter password",type="password")
        button=st.form_submit_button("signup")

            
