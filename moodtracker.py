# Author: Sumeyya Sherief


import gradio as gr
import json
import os
from datetime import datetime

# Path where mood entries will be saved in JSON format
FILE_PATH = os.path.join(os.getcwd(), 'mood_tracker.json')  


def load_entries():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_entries(entries):
    with open(FILE_PATH, 'w') as file:
        json.dump(entries, file, indent=4)

def generate_new_id(entries):
    if entries:
        return max(entry['id'] for entry in entries) + 1
    else:
        return 1

def create_mood_entry(mood, notes=None):
    entries = load_entries()
    new_id = generate_new_id(entries)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = {
        "id": new_id,
        "timestamp": timestamp,
        "mood": mood,
        "notes": notes
    }
    entries.append(entry)
    save_entries(entries)
    return f"Mood entry saved with ID: {new_id}"

def view_mood_entries():
    entries = load_entries()
    if not entries:
        return "No mood entries found."
    else:
        result = []
        for entry in entries:
            entry_str = (f"ID: {entry['id']}\n"
                         f"Timestamp: {entry['timestamp']}\n"
                         f"Mood: {entry['mood']}\n"
                         f"Notes: {entry.get('notes', 'None')}\n"
                         + "-" * 40)
            result.append(entry_str)
        return "\n".join(result)

def edit_mood_entry(entry_id, new_mood, new_notes=None):
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
        return "Entry edited successfully."
    else:
        return "Entry not found."

def delete_mood_entry(entry_id):
    entries = load_entries()
    updated_entries = [entry for entry in entries if entry['id'] != entry_id]
    if len(updated_entries) == len(entries):
        return "Entry not found."
    else:
        save_entries(updated_entries)
        return "Entry deleted successfully."

def mood_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Mood Tracker")

        mood_options = ["Happy", "Sad", "Excited", "Stressed", "Calm", "Anxious", "Angry", "Relaxed"]

        with gr.Tab("Create Entry"):
            mood_input = gr.Radio(label="Select Your Mood", choices=mood_options)
            notes_input = gr.Textbox(label="Notes (Optional)", lines=3)
            create_button = gr.Button("Create Mood Entry")
            create_output = gr.Textbox(label="Message")
            create_button.click(create_mood_entry, inputs=[mood_input, notes_input], outputs=create_output)

        with gr.Tab("View Entries"):
            view_button = gr.Button("View All Entries")
            view_output = gr.Textbox(label="All Mood Entries", lines=10)
            view_button.click(view_mood_entries, outputs=view_output)

        with gr.Tab("Edit Entry"):
            entry_id_input = gr.Number(label="Entry ID", value=None)
            new_mood_input = gr.Radio(label="New Mood", choices=mood_options)
            new_notes_input = gr.Textbox(label="New Notes (Optional)", lines=3)
            edit_button = gr.Button("Edit Mood Entry")
            edit_output = gr.Textbox(label="Edit Message")
            edit_button.click(edit_mood_entry, inputs=[entry_id_input, new_mood_input, new_notes_input], outputs=edit_output)

        with gr.Tab("Delete Entry"):
            entry_id_input = gr.Number(label="Entry ID", value=None)
            delete_button = gr.Button("Delete Mood Entry")
            delete_output = gr.Textbox(label="Delete Message")
            delete_button.click(delete_mood_entry, inputs=[entry_id_input], outputs=delete_output)

    return app
