import streamlit as st
import json
import os

# --- Page Config ---
st.set_page_config(page_title="Eclipse // Exam Intel", layout="centered")

# --- Custom CSS for a Minimalist, High-End Interface ---
st.markdown("""
    <style>
    /* Main App Background */
    .stApp { background-color: #0B0E14; }
    
    /* Branding */
    .header-container {
        text-align: center;
        margin-bottom: 40px;
    }
    .main-title {
        color: #3B82F6;
        font-family: 'Inter', sans-serif;
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 10px;
        letter-spacing: 1px;
    }
    .arabic-dua {
        color: #E5E7EB;
        font-family: 'Inter', sans-serif;
        font-size: 18px;
        font-weight: 500;
        line-height: 1.6;
        direction: rtl;
        margin: 0 auto;
        max-width: 80%;
    }
    .sub-brand {
        color: #4f5b85;
        font-size: 12px;
        letter-spacing: 2px;
        margin-top: 15px;
        font-family: 'Inter', sans-serif;
    }

    /* Search Input Styling */
    div[data-baseweb="input"] {
        background-color: #1C212B !important;
        border-radius: 12px !important;
        border: 1px solid #2D333F !important;
    }
    input {
        color: #E5E7EB !important;
        font-size: 16px !important;
        text-align: center !important;
    }

    /* Card Styling */
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
        font-family: 'Inter', sans-serif;
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
    .details {
        color: #9CA3AF;
        font-size: 14px;
        margin-top: 12px;
        font-family: 'Inter', sans-serif;
    }
    
    /* System Elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- Header Section (Modified for your request) ---
st.markdown("""
    <div class="header-container">
        <p class="main-title">EXAM SCHEDULE</p>
        <p class="arabic-dua">اللهم إني أسألك فهم النبيين وحفظ المرسلين والملائكة المقربين</p>
        <p class="sub-brand">SPRING 2026 FINALS // PORTAL</p>
    </div>
    """, unsafe_allow_html=True)

# --- Centralized Search ---
query = st.text_input("", placeholder="Enter Student ID", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# --- Logic Section ---
if query:
    if os.path.exists("finals2026.json"):
        with open("finals2026.json", "r") as f:
            data = json.load(f).get("Full_Schedule", [])
        
        hits = [e for e in data if query in str(e.get("Students Sets", ""))]
        
        if hits:
            st.markdown(f"<p style='color: #3B82F6; font-weight: bold; font-family: Inter; text-align: center;'>DATA RETRIEVED FOR ID: {query}</p>", unsafe_allow_html=True)
            for exam in hits:
                st.markdown(f"""
                    <div class="exam-card">
                        <p class="subject-title">{exam.get('Subject')}</p>
                        <p class="details">DATE: {exam.get('Day')} &nbsp; | &nbsp; TIME: {exam.get('Time')}</p>
                        <span class="room-badge">ROOM {exam.get('Room')}</span>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("No Records Found. Verify ID.")
    else:
        st.error("System Error: Database link broken.")
else:
    st.markdown("<p style='text-align: center; color: #4f5b85; font-size: 11px; font-family: Inter;'>SYSTEM STATUS: READY</p>", unsafe_allow_html=True)
