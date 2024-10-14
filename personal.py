# Menu Feature
# Personal Tab
# By Aditi Jha
# 10/07/2024

# This file will handle creating, saving, editing, and deleting personal journal entries.


import os
from datetime import datetime

# Path where personal journal entries will be saved
FILE_PATH = 'personal_journal.txt'

def create_personal_entry(content):
    """Create and save a new personal journal entry."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(FILE_PATH, 'a') as file:
        file.write(f"{timestamp} - {content}\n")
    print("Personal entry saved.")

def view_personal_entries():
    """View all personal journal entries."""
    if not os.path.exists(FILE_PATH):
        print("No personal entries found.")
        return
    
    with open(FILE_PATH, 'r') as file:
        entries = file.readlines()
    
    if entries:
        print("Personal Journal Entries:")
        for entry in entries:
            print(entry.strip())
    else:
        print("No personal entries found.")

def edit_personal_entry(old_content, new_content):
    """Edit an existing personal journal entry."""
    if not os.path.exists(FILE_PATH):
        print("No personal entries found.")
        return

    with open(FILE_PATH, 'r') as file:
        entries = file.readlines()

    with open(FILE_PATH, 'w') as file:
        found = False
        for entry in entries:
            if old_content in entry:
                entry = entry.replace(old_content, new_content)
                found = True
            file.write(entry)

    if found:
        print("Entry edited successfully.")
    else:
        print("Entry not found.")

def delete_personal_entry(content):
    """Delete an existing personal journal entry."""
    if not os.path.exists(FILE_PATH):
        print("No personal entries found.")
        return

    with open(FILE_PATH, 'r') as file:
        entries = file.readlines()

    with open(FILE_PATH, 'w') as file:
        found = False
        for entry in entries:
            if content in entry:
                found = True
                continue  # Skip writing this entry back to the file
            file.write(entry)

    if found:
        print("Entry deleted successfully.")
    else:
        print("Entry not found.")
