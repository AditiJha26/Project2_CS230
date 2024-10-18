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

def view_ideas(ideas):
    if not ideas:
        print("No ideas found.")
    else:
        for idx, idea in enumerate(ideas, start=1):
            print(f"{idx}. {idea}")

def add_idea():
    idea = input("Enter your idea: ")
    ideas = load_ideas()
    ideas.append(idea)
    save_ideas(ideas)
    print("Idea saved successfully.")

def delete_idea():
    ideas = load_ideas()
    if not ideas:
        print("No ideas to delete.")
        return
    view_ideas(ideas)
    try:
        idx = int(input("Enter the number of the idea to delete: ")) - 1
        if 0 <= idx < len(ideas):
            deleted_idea = ideas.pop(idx)
            save_ideas(ideas)
            print(f"Idea '{deleted_idea}' deleted successfully.")
        else:
            print("Invalid idea number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def ideas_menu():
    while True:
        print("\nIdeas Menu:")
        print("1. View Ideas")
        print("2. Add Idea")
        print("3. Delete Idea")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            ideas = load_ideas()
            view_ideas(ideas)
        elif choice == '2':
            add_idea()
        elif choice == '3':
            delete_idea()
        elif choice == '4':
            print("Exiting Ideas Menu.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    ideas_menu()
