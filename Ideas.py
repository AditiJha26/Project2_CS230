# Author: Rebecca Rogovich
# 10/14/2024

# This file handles the "Ideas" category, a freeform space where users can quickly 
# jot down ideas, thoughts, or brainstorming sessions without any structure.

import json
import os

ideas_file = 'ideas.json'

def load_ideas():
    if os.path.exists(ideas_file):
        with open(ideas_file, 'r') as file:
            return json.load(file)
    else:
        return []

def save_ideas(ideas):
    with open(ideas_file, 'w') as file:
        json.dump(ideas, file, indent=4)

def view_ideas():
    ideas = load_ideas()
    if not ideas:
        return "No ideas found."
    else:
        return "\n".join([f"{idx+1}. {idea}" for idx, idea in enumerate(ideas)])

def add_idea(new_idea):
    if new_idea.strip() == "":
        return "Idea cannot be empty."
    ideas = load_ideas()
    ideas.append(new_idea)
    save_ideas(ideas)
    return f"Idea '{new_idea}' saved successfully!"

def delete_idea(index):
    try:
        ideas = load_ideas()
        idx = int(index) - 1
        if 0 <= idx < len(ideas):
            deleted_idea = ideas.pop(idx)
            save_ideas(ideas)
            return f"Idea '{deleted_idea}' deleted successfully."
        else:
            return "Invalid idea number."
    except (ValueError, IndexError):
        return "Invalid input. Please enter a valid number."
