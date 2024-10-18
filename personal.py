# Menu Feature
# Personal Tab
# By Aditi Jha
# 10/07/2024

# This file will handle creating, saving, editing, and deleting "personal" journal entries.
# Each Entry is given and ID for better editing and search functions.
# User can add the image by specifying the path of the image when creating a new entry.

import json
import os
from datetime import datetime

# Path where personal journal entries will be saved in JSON format
FILE_PATH = 'personal_journal.json'

def load_entries():
    """Loading all personal journal entries from the JSON file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_entries(entries):
    """Saving all personal journal entries back to the JSON file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(entries, file, indent=4)

def generate_new_id(entries):
    """Generating a unique ID for a new entry."""
    if entries:
        return max(entry['id'] for entry in entries) + 1
    else:
        return 1

def create_personal_entry(content, image_path=None):
    """Creating and saving a new personal journal entry."""
    entries = load_entries()
    new_id = generate_new_id(entries)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "id": new_id,
        "timestamp": timestamp,
        "content": content,
        "category": "personal",
        "image_path": image_path  # Optional image path
    }
    entries.append(entry)
    save_entries(entries)
    print(f"Personal entry saved with ID: {new_id}")

def view_personal_entries():
    """Viewing all personal journal entries."""
    entries = load_entries()
    if not entries:
        print("No personal entries found.")
    else:
        print("Personal Journal Entries:")
        for entry in entries:
            print(f"ID: {entry['id']}")
            print(f"Timestamp: {entry['timestamp']}")
            print(f"Content: {entry['content']}")
            if entry.get("image_path"):
                print(f"Image: {entry['image_path']}")
            print("-" * 40)

def edit_personal_entry(entry_id, new_content):
    """Editing an existing personal journal entry by ID."""
    entries = load_entries()
    found = False
    for entry in entries:
        if entry['id'] == entry_id:
            entry['content'] = new_content
            found = True
            break
    if found:
        save_entries(entries)
        print("Entry edited successfully.")
    else:
        print("Entry not found.")

def delete_personal_entry(entry_id):
    """Deleting an existing personal journal entry by ID."""
    entries = load_entries()
    updated_entries = [entry for entry in entries if entry['id'] != entry_id]
    if len(updated_entries) == len(entries):
        print("Entry not found.")
    else:
        save_entries(updated_entries)
        print("Entry deleted successfully.")