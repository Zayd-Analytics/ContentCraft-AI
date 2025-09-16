import json
import random
import pandas as pd
import os

# ---------- Load Templates ----------
def load_templates(filepath="templates.json"):
    """Load content templates from JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Template file not found: {filepath}")
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------- Hashtag Generator ----------
def generate_hashtags(topic, count=5):
    """Generate random hashtags based on topic."""
    base_hashtags = [
        "Motivation", "Success", "Goals", "Inspiration",
        "AI", "Tech", "Coding", "Productivity",
        "Life", "Hustle", "Mindset", "Innovation"
    ]
    topic_clean = topic.replace(" ", "")
    selected = random.sample(base_hashtags, min(count, len(base_hashtags)))
    return " ".join([f"#{topic_clean}"] + [f"#{tag}" for tag in selected])

# ---------- Emoji Enhancer ----------
def add_emojis(text, mood="Motivational"):
    """Enhance text with emojis based on mood."""
    mood_emojis = {
        "Motivational": ["💪", "🔥", "✨", "🚀"],
        "Funny": ["😂", "🤣", "😎", "🤪"],
        "Professional": ["💼", "📊", "📈", "✅"],
        "Friendly": ["😊", "🤝", "🙌", "🌟"],
        "Serious": ["⚡", "📌", "🔑", "📝"],
        "Storytelling": ["📖", "🎬", "🧩", "🎯"]
    }
    emojis = mood_emojis.get(mood, ["✨", "🚀"])
    return text + " " + " ".join(random.sample(emojis, min(2, len(emojis))))

# ---------- Bulk Export ----------
def export_to_csv(data, filename="generated_content.csv"):
    """Export generated content to CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
    return filename
