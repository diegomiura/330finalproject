import os
import requests
import streamlit as st

_fallback_hf_token = None

# GPT generated fact generator
def get_fact_gpt(token=None):
    """Generates a fun and short astronomy fact using the Hugging Face Inference API with GPT."""
    prompt = "Tell me a short and fun astronomy fact."
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    # Determine the token to use
    if not token:
        try:
            token = st.session_state.get("hf_token", "")
        except:
            token = None
    if not token:
        print("Missing Hugging Face API token.")
        return "Please enter your Hugging Face API token."

    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "inputs": prompt,
        "parameters": {"max_new_tokens": 50, "do_sample": True, "temperature": 0.5},
        "options": {"use_cache": False}
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code != 200:
        print("Error with inference API:", response.status_code, response.text)
        return "Unable to generate fact at this time."
    try:
        generated = response.json()
        if isinstance(generated, list) and "generated_text" in generated[0]:
            return generated[0]["generated_text"].strip()
    except Exception as e:
        print("Error parsing response:", e)
        return "Unable to generate fact at this time."


# For testing purposes, you can call the function directly.
# TODO: Either remove this, or make it work
#       --> The current issue is that if you run `python huggingface_fact_generator.py`,
#           it will not have access to the Streamlit session state, so it will not have
#           the Hugging Face API token.
#       --> You can either set the token manually here for testing, or run it within
#           the Streamlit app.
#       --> Alternatively, you can create a separate script for testing that does not
#           rely on Streamlit session state.
if __name__ == "__main__":
    try:
        token = input("Enter your Hugging Face API token: ").strip()
        fact = get_fact_gpt(token=token)
        print("\nGenerated Astronomy Fact:")
        print(f"⭐ {fact}")
    except Exception as e:
        print(f"Something went wrong: {e}")
