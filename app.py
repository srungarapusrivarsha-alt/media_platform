import streamlit as st 
from db_c import conn,cursor
st.title("Media Platform")


if "user" not in st.session_state:
    st.session_state.user=None
def dashboard():
    st.sidebar.success("Hello User")
    option=st.sidebar.selectbox("choose here:--",["upload_files","view_files","logout"])
    st.header("welcome!!")
    if option=="upload_files":
        choosen_file=st.header("upload your file here",type=["pdf","png","jpg","mp3","mp4"])
        if choosen_file:
            st.write(choosen_file.name)
            st.write(choosen_file.type)
        if "image" in choosen_file.type:
            st.image(choosen_file)
        elif "video" in choosen_file.type:
            st.video(choosen_file)
        elif "audio" in choosen_file:
            st.audio(choosen_file)


        
def login():
    st.header("Login")
    with st.form("Login_Form"):
        email = st.text_input("Email")
        password = st.text_input("Password",type="password")
        btn=st.form_submit_button("Login")
        if btn:
            query="select * from users where email=%s and password=%s"
            values=(email,password)
            cursor.execute(query,values)
            login_user=cursor.fetchone()
            st.session_state.user=login_user
            st.write("logged in successfully")



def signup():
    st.header("SignUp")

    with st.form("SignUp_Form"):

        name = st.text_input("Name")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        btn = st.form_submit_button("SignUp")
        if btn:
            query="insert into users(name,email,password)values(%s , %s , %s)"
            values=(name,email,password)
            cursor.execute(query,values)
            conn.commit()
            st.write("students added successfully")
if st.session_state.user==None:               
    login,signup = st.tabs(
            ["Login","SignUp"]
         )
    with login:
        login()
    with signup:
        signup()
else:
    dashboard()        




