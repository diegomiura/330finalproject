import streamlit as st
from huggingface_fact_generator import get_fact_gpt
from fact_generator import get_fact as get_fact_hardcoded
from datetime import date
import json
import os

st.set_page_config(page_title="Daily Astro Fun Fact ✨")

st.title("🚀 Astronomy Fun Fact of the Day")
st.markdown("Welcome! Get your daily dose of astronomy fun facts here.")

st.sidebar.title("🔐 Hugging Face API")
hf_token_input = st.sidebar.text_input("Enter your Hugging Face API token:", type="password")
if hf_token_input:
    st.session_state["hf_token"] = hf_token_input

# Toggle to choose fact source: GPT-based if checked, otherwise hard-coded
use_gpt = st.checkbox("Use GPT-based fact generation", value=False)

FACT_FILE = "today_fact.json"
LOG_FILE = "fact_log.jsonl"
today = str(date.today())

def load_or_generate_today_fact(use_gpt):
    if os.path.exists(FACT_FILE):
        with open(FACT_FILE, "r") as f:
            data = json.load(f)
            if data.get("date") == today and data.get("fact"):
                return data["fact"]
    # If no valid fact exists for today, generate a new one
    new_fact = get_fact_gpt() if use_gpt else get_fact_hardcoded()
    with open(FACT_FILE, "w") as f:
        json.dump({"date": today, "fact": new_fact}, f)
    return new_fact

def update_fact_log(fact):
    # Retain log entries for days other than today
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
        with open(LOG_FILE, "w") as f:
            for line in lines:
                try:
                    entry = json.loads(line)
                    if entry.get("date") != today:
                        f.write(line)
                except:
                    continue
    with open(LOG_FILE, "a") as f:
        json.dump({"date": today, "fact": fact}, f)
        f.write("\n")

if st.button("🔁 Regenerate today's fact"):
    new_fact = get_fact_gpt() if use_gpt else get_fact_hardcoded()
    with open(FACT_FILE, "w") as f:
        json.dump({"date": today, "fact": new_fact}, f)

    update_fact_log(new_fact)

    st.success("✅ Today's fact has been regenerated!")
    st.rerun()

fact = load_or_generate_today_fact(use_gpt)
st.success(fact)

with st.expander("📜 Show all past facts"):
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            lines = f.readlines()
            for line in reversed(lines):  # newest first
                try:
                    entry = json.loads(line)
                    st.write(f"📅 **{entry['date']}**")
                    st.write(f"✨ {entry['fact']}")
                    st.markdown("---")
                except:
                    continue
    else:
        st.info("No past facts yet.")