import streamlit as st
import streamlit.components.v1 as components
from html import escape
from pathlib import Path

st.set_page_config(
    page_title="Happy Birthday! 🎂",
    page_icon="🎂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# -----------------------------
# Personalize these defaults
# -----------------------------
DEFAULT_NAME = "Monicascade"
DEFAULT_MESSAGE = "May your day be filled with laughter, love, surprises and beautiful memories!"
DEFAULT_FROM = "With lots of love ❤️"

with st.sidebar:
    st.header("🎁 Personalize")
    name = st.text_input("Birthday person's name", MONICA VASIREDDY)
    message = st.text_area("Birthday message", MAN I LIKE U)
    from_text = st.text_input("From", HULK)
    st.caption("Tip: After editing, click outside the field to refresh the greeting.")

name = escape(name.strip() or DEFAULT_NAME)
message = escape(message.strip() or DEFAULT_MESSAGE)
from_text = escape(from_text.strip() or DEFAULT_FROM)

html = Path(__file__).with_name("birthday.html").read_text(encoding="utf-8")
html = html.replace("{{NAME}}", name)
html = html.replace("{{MESSAGE}}", message)
html = html.replace("{{FROM}}", from_text)

components.html(html, height=1050, scrolling=False)
