import streamlit as st
from backend import takecommand,ai


@st.cache_data(show_spinner=False)
def get_output():
    contents = takecommand()
    return ai(contents)

content1 = ""
content2 = ""
content3 = ""

st.set_page_config(layout="wide")
light_mode = {
    "bg": "#FFFFFF",        
    "text": "black",
    "subheader": "#333333",
    "border": "#E0E0E0",
    "sidebar_bg": "#FFFFFF",
    "writing_area": "#E0E0E0" 
}

dark_mode = {
    "bg": "#1E1E1E",       
    "text": "white",
    "subheader": "#F5F5F5",
    "border": "#555555",
    "sidebar_bg": "#1E1E1E", 
    "writing_area": "#333333"  
}

st.sidebar.markdown("## Appearance")
dark_mode_toggle = st.sidebar.checkbox("Dark Mode")

colors = dark_mode if dark_mode_toggle else light_mode

page_bg_color = colors['bg']
sidebar_bg_color = colors['sidebar_bg']
writing_area_bg = colors['writing_area']

st.markdown(
    f"""
    <style>
    .stApp {{
        background-color: {page_bg_color};
    }}

    [data-testid="stSidebar"] {{
        background-color: {sidebar_bg_color} !important;
    }}

    [data-testid="stSidebar"] .css-1n76uvr, 
    [data-testid="stSidebar"] .css-1d391kg, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] label, 
    [data-testid="stSidebar"] span {{
        color: {colors['text']} !important;
    }}

    .stMarkdown, .stText, h3 {{
        color: {colors['text']} !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

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
                background-color: {writing_area_bg}; 
                border-radius: 10px; 
                padding: 20px; 
                height: 300px; 
                overflow: auto;
                color: {colors['text']};
                border-left: 5px solid {colors['border']};
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                ">
                {content1}
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
                background-color: {writing_area_bg}; 
                border-radius: 10px; 
                padding: 20px; 
                height: 300px; 
                overflow: auto;
                color: {colors['text']};
                border-left: 5px solid {colors['border']};
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                ">
                {content2}
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
            background-color: {writing_area_bg}; 
            border-radius: 10px; 
            padding: 20px; 
            height: 200px; 
            overflow: auto;
            color: {colors['text']};
            border-left: 5px solid {colors['border']};
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            ">
            {content3}
        </div>
        """, 
        unsafe_allow_html=True
    )
