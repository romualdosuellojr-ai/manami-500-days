import datetime
import time
import streamlit as st

# 1. Page Configuration (Browser Title and Layout)
st.set_page_config(page_title="Our 500 Days of Love", page_icon="🌸", layout="centered")

# Custom visual styling for a clean pink theme
st.markdown("""
    <style>
    .stApp { background-color: #fff0f5; }
    h1 { color: #d147a3 !important; text-align: center; font-size: 2.5rem !important; }
    .stText, p, div { color: #4a4a4a; font-size: 1.25rem; text-align: center; }
    .heart { font-size: 1.5rem; text-align: center; line-height: 1.2; color: #ff4d4d; }
    </style>
""", unsafe_with_html=True)

# 2. Anniversary Details & Day Calculation
partner_name = "Manami"
start_date = datetime.date(2025, 3, 23)
today = datetime.date.today()
days_together = (today - start_date).days

# 3. Dynamic Title Header
st.markdown(f"<h1>🌸 HAPPY {days_together} DAYS OF LOVE! 🌸</h1>")
st.write("---")

# 4. Typewriter Animation Script
message_lines = [
    f"Today marks exactly {days_together} beautiful days since March 23, 2025.",
    "Thank you for filling my life with so much joy and sweetness.",
    "",
    "✨ My message to you:",
    f"To {partner_name}, happy {days_together} days anniversary of being together!",
    "Thank you for always making me happy. I will love you forever. ❤️"
]

text_placeholder = st.empty()
complete_text = ""

# Simulate live web typewriter effect
for line in message_lines:
    for char in line:
        complete_text += char
        html_text = complete_text.replace("\n", "<br>")
        text_placeholder.markdown(f"<div style='line-height:1.8;'>{html_text}</div>", unsafe_with_html=True)
        time.sleep(0.04)
    complete_text += "\n\n"

st.write("---")
time.sleep(1.0)

# 5. Interactive Balloons Surprise
st.balloons()

# 6. Cherry Blossom Emoji Heart
heart_art = """
<div class='heart'>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸&nbsp;&nbsp;&nbsp;🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸🌸🌸<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🌸<br>
</div>
"""
st.markdown(heart_art, unsafe_with_html=True)
