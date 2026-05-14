import streamlit as st
import json
import os

# --- Page Config ---
st.set_page_config(page_title="Eclipse // Exam Intel", layout="centered")

# --- Custom CSS for Perfect Centering ---
st.markdown("""
    <style>
    .stApp { background-color: #0B0E14; }
    
    /* Perfect Center Header Wrapper */
    .header-wrapper {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        width: 100%;
        margin-bottom: 40px;
        padding-top: 20px;
    }

    .main-title {
        color: #3B82F6;
        font-family: 'Inter', sans-serif;
        font-size: clamp(28px, 5vw, 42px); /* Responsive font size */
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

    .sub-brand {
        color: #4f5b85;
        font-size: 11px;
        letter-spacing: 3px;
        margin-top: 20px;
        text-transform: uppercase;
    }

    /* Input Box Centering */
    div[data-baseweb="input"] {
        background-color: #1C212B !important;
        border-radius: 12px !important;
        border: 1px solid #2D333F !important;
        max-width: 500px;
        margin: 0 auto !important;
    }
    
    input {
        color: #E5E7EB !important;
        font-size: 16px !important;
        text-align: center !important;
    }

    /* Result Card Styling */
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
    
    /* UI Cleanup */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Updated Centered Header ---
st.markdown("""
    <div class="header-wrapper">
        <div class="main-title">Exam Schedule</div>
        <div class="arabic-dua">اللهم إني أسألك فهم النبيين وحفظ المرسلين والملائكة المقربين</div>
        <div class="sub-brand">Spring 2026 Finals // Portal</div>
    </div>
    """, unsafe_allow_html=True)

# --- Search Section ---
# Using a container to ensure the input itself stays centered
query = st.text_input("", placeholder="Enter Student ID", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# --- Search Logic ---
if query:
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
            st.error("No Records Found.")
    else:
        st.error("Database missing.")
else:
    st.markdown("<p style='text-align: center; color: #4f5b85; font-size: 10px;'>SYSTEM STATUS: ONLINE</p>", unsafe_allow_html=True)
