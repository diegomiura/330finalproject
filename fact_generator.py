# fact_generator.py

import random

# You can expand or replace this list with GPT-generated facts later
# (This short list was given to me by ChatGPT)
FUN_FACTS = [
    "Neutron stars can spin 600 times per second! 💫",
    "A day on Venus is longer than a year on Venus. 😮",
    "The largest volcano in the Solar System is on Mars — Olympus Mons.",
    "There are more stars in the universe than grains of sand on Earth.",
    "Jupiter’s moon Europa might have an ocean beneath its icy crust. 🌊🧊",
    "Light from the Sun takes about 8 minutes to reach Earth. ☀️➡️🌍",
    "The Moon is slowly drifting away from Earth — about 3.8 cm per year.",
    "Black holes can warp spacetime so strongly that time slows down near them. ⏳"
]

def get_fact():
    """Return a random astronomy fun fact."""
    return random.choice(FUN_FACTS)

# Quick test
if __name__ == "__main__":
    print(get_fact())