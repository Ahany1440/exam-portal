import streamlit as st
import json
import os

# --- Page Config ---
st.set_page_config(page_title="Eclipse // Exam Intel", layout="centered")

# --- Custom CSS for Perfect Centering & Form Styling ---
st.markdown("""
    <style>
    .stApp { background-color: #0B0E14; }
    
    .header-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        margin-bottom: 40px;
    }

    .main-title {
        color: #3B82F6;
        font-family: 'Inter', sans-serif;
        font-size: clamp(28px, 5vw, 42px);
        font-weight: bold;
        margin: 0;
        text-transform: uppercase;
        letter-spacing: 2px;
    }

    .arabic-dua {
        color: #E5E7EB;
        font-family: 'Inter', sans-serif;
        font-size: clamp(16px, 4vw, 20px);
        font-weight: 500;
        line-height: 1.6;
        direction: rtl;
        margin-top: 10px;
        max-width: 90%;
    }

    /* Form and Button Styling */
    .stForm {
        border: none !important;
        padding: 0 !important;
    }
    
    div[data-baseweb="input"] {
        background-color: #1C212B !important;
        border-radius: 12px !important;
        border: 1px solid #2D333F !important;
    }
    
    input {
        color: #E5E7EB !important;
        text-align: center !important;
    }

    /* Custom Button Styling */
    .stButton > button {
        width: 100%;
        background-color: #3B82F6 !important;
        color: white !important;
        border-radius: 12px !important;
        border: none !important;
        height: 50px;
        font-weight: bold !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        transition: 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #2563EB !important;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.4);
    }

    .exam-card {
        background-color: #151921;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #232833;
        margin-bottom: 20px;
    }
    .subject-title {
        color: #E5E7EB;
        font-size: 22px;
        font-weight: bold;
        margin: 0;
    }
    .room-badge {
        background-color: #1E293B;
        color: #3B82F6;
        padding: 6px 14px;
        border-radius: 8px;
        font-family: 'Consolas', monospace;
        font-weight: bold;
        display: inline-block;
        margin-top: 10px;
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown("""
    <div class="header-wrapper">
        <div class="main-title">Exam Schedule</div>
        <div class="arabic-dua">اللهم إني أسألك فهم النبيين وحفظ المرسلين والملائكة المقربين</div>
    </div>
    """, unsafe_allow_html=True)

# --- The Search Form (Removes "Press Enter to apply") ---
with st.form("search_form", clear_on_submit=False):
    query = st.text_input("", placeholder="Enter Student ID", label_visibility="collapsed")
    submit = st.form_submit_button("Find My Schedule")

st.markdown("<br>", unsafe_allow_html=True)

# --- Logic ---
if submit and query:
    if os.path.exists("finals2026.json"):
        with open("finals2026.json", "r") as f:
            data = json.load(f).get("Full_Schedule", [])
        
        hits = [e for e in data if query in str(e.get("Students Sets", ""))]
        
        if hits:
            st.markdown(f"<p style='color: #3B82F6; font-weight: bold; text-align: center;'>RESULTS FOR ID: {query}</p>", unsafe_allow_html=True)
            for exam in hits:
                st.markdown(f"""
                    <div class="exam-card">
                        <p class="subject-title">{exam.get('Subject')}</p>
                        <p style="color:#9CA3AF; font-size:14px; margin-top:10px;">
                            DATE: {exam.get('Day')} &nbsp; | &nbsp; TIME: {exam.get('Time')}
                        </p>
                        <span class="room-badge">ROOM {exam.get('Room')}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("No Records Found. Please verify your ID.")
    else:
        st.error("Database connection error.")
elif submit and not query:
    st.warning("Please enter an ID first.")
