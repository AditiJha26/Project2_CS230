# Mood Tracker Tab
# By Sumeyya Sherief
# 10/14/2024

# This file will handle creating, saving, editing, and deleting mood entries.
# Each Entry is given and ID for better editing and search functions.
# User can add the mood and optional notes when creating a new entry.

import json
import os
from datetime import datetime

# Path where mood entries will be saved in JSON format
FILE_PATH = 'mood_tracker.json'

def load_entries():
    """Loading all mood entries from the JSON file."""
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_entries(entries):
    """Saving all mood entries back to the JSON file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(entries, file, indent=4)

def generate_new_id(entries):
    """Generating a unique ID for a new entry."""
    if entries:
        return max(entry['id'] for entry in entries) + 1
    else:
        return 1

def create_mood_entry(mood, notes=None):
    """Creating and saving a new mood entry."""
    entries = load_entries()
    new_id = generate_new_id(entries)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "id": new_id,
        "timestamp": timestamp,
        "mood": mood,
        "notes": notes  # Optional notes
    }
    entries.append(entry)
    save_entries(entries)
    print(f"Mood entry saved with ID: {new_id}")

def view_mood_entries():
    """Viewing all mood entries."""
    entries = load_entries()
    if not entries:
        print("No mood entries found.")
    else:
        print("Mood Tracker Entries:")
        for entry in entries:
            print(f"ID: {entry['id']}")
            print(f"Timestamp: {entry['timestamp']}")
            print(f"Mood: {entry['mood']}")
            if entry.get("notes"):
                print(f"Notes: {entry['notes']}")
            print("-" * 40)

def edit_mood_entry(entry_id, new_mood, new_notes=None):
    """Editing an existing mood entry by ID."""
    entries = load_entries()
    found = False
    for entry in entries:
        if entry['id'] == entry_id:
            entry['mood'] = new_mood
            entry['notes'] = new_notes
            found = True
            break
    if found:
        save_entries(entries)
        print("Entry edited successfully.")
    else:
        print("Entry not found.")

def delete_mood_entry(entry_id):
    """Deleting an existing mood entry by ID."""
    entries = load_entries()
    updated_entries = [entry for entry in entries if entry['id'] != entry_id]
    if len(updated_entries) == len(entries):
        print("Entry not found.")
    else:
        save_entries(updated_entries)
        print("Entry deleted successfully.")

def show_mood_menu():
    """Displaying the Mood Tracker menu and handle user input - Aditi - 10/14/2024"""
    while True:
        print("\nMood Tracker Menu")
        print("1. Create a new mood entry")
        print("2. View all mood entries")
        print("3. Edit a mood entry")
        print("4. Delete a mood entry")
        print("5. Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            mood = input("Enter your mood: ")
            notes = input("Enter any notes (or leave blank): ")
            notes = notes if notes else None
            moodtracker.create_mood_entry(mood, notes)
        elif choice == '2':
            moodtracker.view_mood_entries()
        elif choice == '3':
            try:
                entry_id = int(input("Enter the ID of the mood entry you want to edit: "))
                new_mood = input("Enter the new mood: ")
                new_notes = input("Enter the new notes (or leave blank): ")
                new_notes = new_notes if new_notes else None
                moodtracker.edit_mood_entry(entry_id, new_mood, new_notes)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        elif choice == '4':
            try:
                entry_id = int(input("Enter the ID of the mood entry you want to delete: "))
                moodtracker.delete_mood_entry(entry_id)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    show_mood_menu() 