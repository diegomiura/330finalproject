import os
import requests
from credentials import HUGGINGFACE_API_TOKEN


def get_fact_gpt():
    """Generates a fun and short astronomy fact using the Hugging Face Inference API with GPT-2."""
    prompt = ("Provide one concise, accurate, and fascinating astronomy fact "
          "that is both engaging and informative, expressed in one sentence.")
    API_URL = "https://api-inference.huggingface.co/models/gpt2"
    headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}
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
        # Expecting a list of outputs; extract the generated text
        fact = generated[0].get("generated_text", "").strip()
        return fact
    except Exception as e:
        print("Error parsing response:", e)
        return "Unable to generate fact at this time."


# For testing purposes, you can call the function directly.
if __name__ == '__main__':
    print(get_fact_gpt())
