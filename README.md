# Astro Today
Astro Today is a repository with CLI and Streamlit functionality. It delivers a new astronomy fun fact every day using either a hard-coded list of facts or real-time generation powered by Hugging Face's GPT models. It also integrates with Reddit, allowing users to post these facts directly to a subreddit with a single click.

---

`Warning: The reddit functionality is currently down. The r/astro330 subreddit was banned...`

---

## Before we start
To take full advantage of this project, there are 2 suggestions.
### Hugging Face Account
If you wish to be able to use GPT models to generate fun facts in real time, you must do the following:
1. Create a [Hugging Face](https://huggingface.co/) account
2. Navigate to Settings > Access Tokens > Create New Token
3. Make a token with the 'Write' token type.
4. Store the token somewhere safe.
### Reddit Account
If you wish to post your fun fact to [Reddit](https://www.reddit.com/), you will need an account with a username and password.

---

## How to Access Deployed Streamlit App
[Streamlit App](https://diegomiura-330finalproject-streamlit-app-ljdstr.streamlit.app/)

## How to Run the Streamlit App Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/diegomiura/330finalproject.git
   cd 330finalproject
   ```
2. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app
   ```bash
   streamlit run streamlit_app.py
   ```
## How to Print Fun Fact in Terminal
   Make sure you are in the `330finalproject` directory
   ### Hard-Coded Fact
   ```bash
   python fact_generator.py
   ```
   ### GPT Fact
   ```bash
   python huggingface_fact_generator.py
   ```
   It will ask you to input your hugging face API token. Once you do, hit enter. It will load for a few seconds before outputting the fun fact.
   
## How to post onto Reddit from Terminal
   New instructions coming soon once this functionality is restored...
