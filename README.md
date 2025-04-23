# 🚀 Astro Today – Astronomy Fun Fact Generator

Astro Today is a web app that delivers a new astronomy fun fact every day using either a hard-coded database or real-time generation powered by Hugging Face's GPT models. It also integrates with Reddit, allowing users to post these facts directly to a subreddit with a single click.

---

## 🌟 Features

- 🧠 **AI-Powered Facts**: Generate short astronomy facts using Hugging Face's `flan-t5` or another instruct model.
- 📜 **Hard-Coded Facts**: Option to fall back to a list of manually curated space facts.
- 📬 **Reddit Integration**: Post daily facts to Reddit from within the app.
- 🌌 **NASA APOD Display**: View NASA’s Astronomy Picture of the Day, complete with caption and explanation.
- 🗂️ **Fact Archive**: Keeps a log of all previously generated and posted facts.

---

## 📦 Technologies Used

- **Python**
- **Streamlit**
- **Hugging Face Inference API**
- **PRAW (Python Reddit API Wrapper)**
- **NASA APOD API**

---

## 🚀 How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/astro-fun-facts.git
   cd astro-fun-facts
