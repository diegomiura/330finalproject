import requests
from credentials import HUGGINGFACE_API_TOKEN

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"
headers = {"Authorization": f"Bearer {HUGGINGFACE_API_TOKEN}"}

def get_gpt_fact():
    prompt = "Tell me one short and fun astronomy fact."
    response = requests.post(
        API_URL,
        headers=headers,
        json={
            "inputs": prompt,
            "parameters": {
                "do_sample": True,
                "temperature": 0.9,
                "top_p": 0.95
            }
        }
    )
    if response.status_code == 200:
        data = response.json()
        full_response = data[0]["generated_text"]
        cleaned = full_response.replace(prompt, "").strip()
        return cleaned
    else:
        return "Astronomy fact unavailable today! 🌌"

if __name__ == "__main__":
    print(get_gpt_fact())
