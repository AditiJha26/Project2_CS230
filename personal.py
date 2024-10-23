# Personal Tab of the Journal App:
# AUthor: Aditi Jha
# Last updated: October 23, 2024

# The following code offers these functionality: This file will handle creating, saving, editing, viewing, and deleting personal entries.
# Each Entry is given an ID for better editing and search functions.
# User can also add images while creating new entries or add images after the entry has been created.

import json
import os
from datetime import datetime
from PIL import Image
import io
import base64

# Path where personal journal entries will be saved in JSON format
FILE_PATH = os.path.join(os.getcwd(), 'personal_journal.json')  
IMAGE_DIR = 'images'

# Ensuring the images directory exists
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

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

def create_personal_entry(content, image_data=None):
    """Creating and saving a new personal journal entry with optional image."""
    entries = load_entries()
    new_id = generate_new_id(entries)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "id": new_id,
        "timestamp": timestamp,
        "content": content,
        "category": "personal",
        "image_path": None
    }
    if image_data:
        try:
            image_path = os.path.join(IMAGE_DIR, f"{new_id}.png")
            image = Image.open(io.BytesIO(base64.b64decode(image_data)))
            image.save(image_path)
            entry["image_path"] = image_path
        except Exception as e:
            return f"Failed to save image: {str(e)}"
    entries.append(entry)
    save_entries(entries)
    return f"Entry {new_id} created successfully with{'out' if image_data is None else ''} image."

def view_personal_entries():
    """Viewing all personal journal entries."""
    return load_entries()

def search_entry_by_id(entry_id):
    """Searching for a specific journal entry by ID."""
    entries = load_entries()
    for entry in entries:
        if entry['id'] == entry_id:
            return entry
    return None

def edit_personal_entry(entry_id, new_content):
    """Editing an existing personal journal entry by ID."""
    entries = load_entries()
    found = False
    entry_id = int(entry_id)  # Ensure ID is treated as integer
    for entry in entries:
        if entry['id'] == entry_id:
            entry['content'] = new_content
            found = True
            break
    if found:
        save_entries(entries)
        return "Entry edited successfully."
    else:
        return "Entry not found."

def delete_personal_entry(entry_id):
    """Deleting an existing personal journal entry by ID."""
    entries = load_entries()
    entry_id = int(entry_id)  # Ensure ID is treated as integer
    updated_entries = [entry for entry in entries if entry['id'] != entry_id]
    if len(updated_entries) == len(entries):
        return "Entry not found."
    else:
        save_entries(updated_entries)
        return "Entry deleted successfully."

def add_image_to_entry(entry_id, image_data):
    """Adding an image to an existing entry by ID."""
    entries = load_entries()
    found = False
    for entry in entries:
        if entry['id'] == int(entry_id):
            try:
                image_path = os.path.join(IMAGE_DIR, f"{entry_id}.png")
                image = Image.open(io.BytesIO(base64.b64decode(image_data)))
                image.save(image_path)
                entry['image_path'] = image_path
                found = True
                break
            except Exception as e:
                print(f"Failed to add image: {str(e)}")
    if found:
        save_entries(entries)
        return f"Image successfully added to entry ID {entry_id}."
    else:
        return "Entry not found or invalid image data."