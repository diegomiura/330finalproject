import os
import requests
import streamlit as st

def get_fact_gpt():
    """Generates a fun and short astronomy fact using the Hugging Face Inference API with GPT-2."""
    prompt = "Tell me a short and fun astronomy fact."
    API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

    hf_token = st.session_state.get("hf_token", "")
    if not hf_token:
        print("Missing Hugging Face API token.")
        return "Please enter your Hugging Face API token in the sidebar."
    headers = {"Authorization": f"Bearer {hf_token}"}
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
            fact = generated[0]["generated_text"].strip()
            return fact
    except Exception as e:
        print("Error parsing response:", e)
        return "Unable to generate fact at this time."


# For testing purposes, you can call the function directly.
if __name__ == '__main__':
    print(get_fact_gpt())
