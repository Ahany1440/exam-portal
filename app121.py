import streamlit as st
import json
import os

# --- Page Config & Styling ---
st.set_page_config(page_title="Eclipse // Exam Intel", page_icon="🌙", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0B0E14; }
    .stApp { background-color: #0B0E14; }
    
    /* Card Styling */
    .exam-card {
        background-color: #151921;
        padding: 25px;
        border-radius: 16px;
        border: 1px solid #232833;
        margin-bottom: 15px;
    }
    .subject-title {
        color: #E5E7EB;
        font-size: 24px;
        font-weight: bold;
        margin: 0;
    }
    .room-badge {
        background-color: #1E293B;
        color: #3B82F6;
        padding: 5px 15px;
        border-radius: 8px;
        font-family: 'Consolas', monospace;
        font-weight: bold;
        float: right;
    }
    .details {
        color: #9CA3AF;
        font-size: 14px;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.markdown("<h1 style='color: #3B82F6; text-align: center;'>يارب ننجح و نقفل</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #4f5b85;'>SPRING 2026 FINALS</p>", unsafe_allow_html=True)
    st.divider()
    query = st.text_input("Enter ID Number", placeholder="25100xxxx")
    search_clicked = st.button("Search Courses", use_container_width=True)

# --- Main Content ---
if query or search_clicked:
    if os.path.exists("finals2026.json"):
        with open("finals2026.json", "r") as f:
            data = json.load(f).get("Full_Schedule", [])
        
        hits = [e for e in data if query in str(e.get("Students Sets", ""))]
        
        if hits:
            st.markdown(f"<h2 style='color: #3B82F6;'>ID: {query}</h2>", unsafe_allow_html=True)
            for exam in hits:
                st.markdown(f"""
                    <div class="exam-card">
                        <span class="room-badge">ROOM {exam.get('Room')}</span>
                        <p class="subject-title">{exam.get('Subject')}</p>
                        <p class="details">📅 {exam.get('Day')} &nbsp; | &nbsp; 🕒 {exam.get('Time')}</p>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.error("No Records Found. Verify the ID.")
    else:
        st.error("Database file missing.")
else:
    st.markdown("<h2 style='color: #E5E7EB;'>Systems Ready</h2>", unsafe_allow_html=True)
    st.info("Enter your ID in the sidebar to retrieve your schedule.")