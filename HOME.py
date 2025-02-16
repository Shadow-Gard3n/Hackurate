import streamlit as st
from backend import takecommand, ai
import time


# signup
def signup():
    if "Information" not in st.session_state:
        st.session_state.Information = {"Name": "",
                                        "Username": "",
                                        "Password": ""}

    with st.form(key="signuppage"):
        st.session_state.Information["Name"] = st.text_input("Enter your Name")
        st.session_state.Information["Username"] = st.text_input("Enter your Username")
        st.session_state.Information["Password"] = st.text_input("Enter your Password", type="password")
        submitButton = st.form_submit_button(label="Submit")
        if submitButton:
            # TODO authentication logic
            st.success("Signup Successful!")
            st.session_state.page = 1  
            st.rerun()  

    st.caption("Already have an Account?")
    if st.button("Login"):
        st.session_state.page = 1
        st.rerun()  


# login
def login():
    if "Authentication" not in st.session_state:
        st.session_state.Authentication = {"Username": "",
                                            "Password": ""}

    with st.form(key="loginpage"):
        st.session_state.Authentication["Username"] = st.text_input("Enter your Username")
        st.session_state.Authentication["Password"] = st.text_input("Enter your Password", type="password")
        submitButton = st.form_submit_button(label="Submit")

        if submitButton:
            # TODO authentication logic
            if (st.session_state.Authentication["Username"] == "admin" and 
                st.session_state.Authentication["Password"] == "password"):
                st.success("Login Successful!")
                st.session_state.page = 2
                st.rerun()  
            else:
                st.error("Invalid Username or Password")

    st.caption("No Account Yet?")
    if st.button("Signup"):
        st.session_state.page = 0
        st.rerun()  


# home
def home():
    st.set_page_config(layout="wide")

    if 'contents' not in st.session_state:
        st.session_state.contents = ""
    if 'content1' not in st.session_state:
        st.session_state.content1 = ""
    if 'content2' not in st.session_state:
        st.session_state.content2 = ""
    if 'listening' not in st.session_state:
        st.session_state.listening = True  

    lightmode = {
        "bg": "#00FFFF",
        "text": "black",
        "subheader": "black",
        "border": "black",
        "writing_area": "#F0F8FF",
        "button_bg": "black",
        "button_text": "#00FFFF"
    }
    
    darkmode = {
        "bg": "#2E2E2E",
        "text": "#E0E0E0",
        "subheader": "#E0E0E0",
        "border": "black",
        "writing_area": "#000000",
        "button_bg": "#000000",
        "button_text": "#E0E0E0"
    }

    st.markdown("## Appearance")
    toggle = st.checkbox("Dark Mode")

    colors = darkmode if toggle else lightmode

    st.markdown(
        f"""
        <style>
            .stApp {{
                background-color: {colors['bg']};
                color: {colors['text']};
            }}
            .stButton>button {{
                background-color: {colors['button_bg']};
                color: {colors['button_text']};
                border: none;
                border-radius: 5px;
                padding: 0.5em 1em;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s;
            }}
            .stButton>button:hover {{
                background-color: #357ABD;
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    if st.button("RESTART"):
        st.session_state.listening = True
        st.rerun()

    col1, col2 = st.columns(2, gap="small")

    with col1:
        st.markdown(
            f"<h3 style='color:{colors['subheader']};'>Potential Diagnosis</h3>",
            unsafe_allow_html=True
        )
        with st.container():
            st.markdown(
                f"""
                <div style="
                    background-color: {colors['writing_area']}; 
                    border-radius: 10px; 
                    padding: 20px; 
                    height: 300px; 
                    overflow: auto;
                    color: {colors['text']};
                    border-left: 5px solid {colors['border']};
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    ">
                    {st.session_state.content1}
                </div>
                """, 
                unsafe_allow_html=True
            )

    with col2:
        st.markdown(
            f"<h3 style='color:{colors['subheader']};'>Suggested Questions</h3>",
            unsafe_allow_html=True
        )
        with st.container():
            st.markdown(
                f"""
                <div style="
                    background-color: {colors['writing_area']}; 
                    border-radius: 10px; 
                    padding: 20px; 
                    height: 300px; 
                    overflow: auto;
                    color: {colors['text']};
                    border-left: 5px solid {colors['border']};
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                    ">
                    {st.session_state.content2}
                </div>
                """, 
                unsafe_allow_html=True
            )

    st.markdown(
        f"<h3 style='color:{colors['subheader']};'>Your Conversation</h3>",
        unsafe_allow_html=True
    )
    with st.container():
        st.markdown(
            f"""
            <div style="
                background-color: {colors['writing_area']}; 
                border-radius: 10px; 
                padding: 20px; 
                height: 200px; 
                overflow: auto;
                color: {colors['text']};
                border-left: 5px solid {colors['border']};
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                ">
                {st.session_state.contents}
            </div>
            """, 
            unsafe_allow_html=True
        )

    st.write("")
    st.write("")
    if st.button("FINISH"):
        st.session_state.listening = False
    
    if st.session_state.listening:
        contents = takecommand()
        if contents != st.session_state.contents:
            st.session_state.contents = contents
            st.session_state.content1 += "\n\n\n\n" + ai(st.session_state.contents)
            st.rerun()

        time.sleep(2)  
        st.rerun()

if 'page' not in st.session_state:
    st.session_state.page = 1  
    
if st.session_state.page == 0:
    signup()
elif st.session_state.page == 1:
    login()
elif st.session_state.page == 2:
    home()
