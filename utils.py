import json
from difflib import get_close_matches

def load_faq(filepath="faq_data.json"):
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading FAQ file: {e}")
        return {}

def find_best_match(user_input, faq_data):
    questions = list(faq_data.keys())
    match = get_close_matches(user_input, questions, n=1, cutoff=0.5)
    return match[0] if match else None
