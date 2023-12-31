from __future__ import annotations

import streamlit as st

from src.streamlit import widgets
from src.utils import config

# Initialize session state variables if they don't exist yet
if "current_question" not in st.session_state:
    st.session_state.answers = {}
    st.session_state.current_question = 0
    st.session_state.questions = []
    st.session_state.right_answers = 0
    st.session_state.wrong_answers = 0

# Set Page Configuration
st.set_page_config(
    page_title=config.config()["app"]["page_title"],
    page_icon=config.config()["app"]["page_icon"],
)
st.title(config.config()["app"]["title"])

# Sidebar Enablement
st.sidebar.success(config.config()["app"]["sidebar"])

# Add App Onboarding
st.markdown(
    "\n\n".join(config.config()["app"]["onboarding"]),
)
st.divider()

# Create a 3-column layout for the Prev/Next buttons and the question display
col1, col2, col3 = st.columns([1, 6, 1])

# Add a Prev button to the left column that goes to the previous question
with col1:
    if col1.button(config.config()["app"]["quiz"]["prev"]):
        widgets.prev_question()

# Add a Next button to the right column that goes to the next question
with col3:
    if col3.button(config.config()["app"]["quiz"]["next"]):
        widgets.next_question_v2()

# Display the actual quiz question
with col2:
    widgets.display_question_v2()
