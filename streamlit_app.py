import streamlit as st
from huggingface_fact_generator import get_fact_gpt
from fact_generator import get_fact as get_fact_hardcoded
from datetime import date
import json
import os
import praw
import requests
from reddit_bot import post_fact_to_reddit


# File paths
FACT_FILE = "today_fact.json"
LOG_FILE = "fact_log.jsonl"
today = str(date.today())



# Display NASA's Astronomy Picture of the Day (APOD)
def display_apod_image():
    apod_url = "https://api.nasa.gov/planetary/apod"
    params = {"api_key": "DEMO_KEY"}  # Replace with your actual key if available
    try:
        response = requests.get(apod_url, params=params)
        if response.status_code == 200:
            data = response.json()
            image_url = data.get("url")
            title = data.get("title", "Astronomy Picture of the Day")
            explanation = data.get("explanation", "")
            if image_url:
                st.image(image_url, caption=title, use_container_width=False)
                with st.expander("📖 About this image"):
                    st.markdown(explanation)
    except Exception as e:
        st.warning(f"Could not load APOD: {e}")



# Title and description
st.set_page_config(page_title="🚀Astro Today✨", layout="wide")
st.title("🚀Astro Today✨")
st.subheader("Welcome! Get your daily dose of astronomy here.")



### Sidebar ###
st.sidebar.title("🔐 Hugging Face API")

# Hugging Face API token
hf_token_input = st.sidebar.text_input("Enter your Hugging Face API token:", type="password")
if hf_token_input:
    st.session_state["hf_token"] = hf_token_input

# Reddit API credentials
st.sidebar.title("🤖 Reddit API Credentials")
#client_id = st.sidebar.text_input("Client ID")
client_id = 'xvo81sTcK1TdTixapCIAaQ'
#client_secret = st.sidebar.text_input("Client Secret", type="password")
client_secret = '0SCgz07cKf13OghqoFu7Zd9anBWvmA'
username = st.sidebar.text_input("Reddit Username")
password = st.sidebar.text_input("Reddit Password", type="password")
#user_agent = st.sidebar.text_input("User Agent")
user_agent = 'a330project by /u/JuggernautKey1263'

# Store in session state
if all([client_id, client_secret, username, password, user_agent]):
    st.session_state["reddit_creds"] = {
        "client_id": client_id,
        "client_secret": client_secret,
        "username": username,
        "password": password,
        "user_agent": user_agent,
    }



# Toggle to choose fact source: GPT-based if checked, otherwise hard-coded
use_gpt = st.checkbox("Use GPT-based fact generation", value=False)



# Making the columns
col1, col2 = st.columns([1, 1])

with col2:
    st.subheader("Astronomy Picture of the Day")
    display_apod_image()


# Function to load or generate today's fact
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




# Function to update the log file
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


with col1:
    st.subheader("Today's Astronomy Fact")

    # Load or generate today's fact
    fact = load_or_generate_today_fact(use_gpt)
    st.success(fact)

    col11, col12 = st.columns([1, 1])
    with col11:
    # Regenerate today's fact
        if st.button("🔁 Regenerate today's fact"):
            new_fact = get_fact_gpt() if use_gpt else get_fact_hardcoded()
            with open(FACT_FILE, "w") as f:
                json.dump({"date": today, "fact": new_fact}, f)

            update_fact_log(new_fact)

            st.success("✅ Today's fact has been regenerated!")
            st.rerun()
    with col12:
        if st.button("📬 Post this fact to Reddit"):
            try:
                creds = st.session_state.get("reddit_creds", {})
                submission = post_fact_to_reddit(fact, creds, subreddit_name="astro330")
                st.success(f"✅ Successfully posted to r/{submission.subreddit.display_name}: {submission.title}")
            except Exception as e:
                st.error(f"Failed to post to Reddit: {e}")
        
    # Update the log file with today's fact
    update_fact_log(fact)


    # Show all past facts
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