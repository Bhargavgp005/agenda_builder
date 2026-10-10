import streamlit as st
import os
from dotenv import load_dotenv
from utils.generator import generate_agenda

# Load env variables
load_dotenv()

st.set_page_config(
    page_title="Gen AI Agenda Builder",
    page_icon="📅",
    layout="centered"
)

# Custom CSS for better aesthetics
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #1e3a8a;
    }
    .stButton>button {
        background-color: #1e3a8a;
        color: white;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: #1e40af;
        border-color: #1e40af;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

st.title("📅 Gen AI Meeting Agenda Builder")
st.markdown("Generate structured, time-boxed meeting agendas using Anthropic's Claude AI.")

with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = st.text_input(
        "Anthropic API Key", 
        type="password", 
        value=os.getenv("ANTHROPIC_API_KEY", ""),
        help="Get your API key from console.anthropic.com"
    )
    st.markdown("---")
    st.markdown("Built with Streamlit & Anthropic")

st.subheader("Meeting Details")
col1, col2 = st.columns([3, 1])

with col1:
    topic = st.text_input("Meeting Topic", placeholder="e.g., Q3 Marketing Strategy Alignment")
with col2:
    duration = st.number_input("Duration (min)", min_value=15, max_value=480, value=60, step=15)

description = st.text_area(
    "Meeting Description & Goals", 
    placeholder="What are the main objectives? Who is attending? Any specific topics to cover?",
    height=150
)

if st.button("✨ Generate Agenda", use_container_width=True):
    if not api_key:
        st.error("Please provide your Anthropic API Key in the sidebar.")
    elif not topic:
        st.warning("Please provide a Meeting Topic.")
    else:
        with st.spinner("Generating your professional agenda..."):
            try:
                agenda_md = generate_agenda(
                    api_key=api_key,
                    topic=topic,
                    description=description,
                    duration=duration
                )
                
                st.success("Agenda generated successfully!")
                
                st.markdown("---")
                st.subheader("Your Generated Agenda")
                st.markdown(agenda_md)
                
                st.markdown("---")
                st.download_button(
                    label="📥 Download Agenda as Markdown",
                    data=agenda_md,
                    file_name="meeting_agenda.md",
                    mime="text/markdown",
                    use_container_width=True
                )
                
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
