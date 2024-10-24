# Author: Rebecca Rogovich

import json
import os
import gradio as gr

ideas_file = os.path.join(os.getcwd(), 'ideas.json')  


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

def ideas_interface():
    with gr.Blocks() as demo:
        gr.Markdown("# Ideas")

        idea_input = gr.Textbox(label="Enter your idea", placeholder="Type your idea here...")
        add_button = gr.Button("Add Idea")
        add_output = gr.Textbox(label="Message", interactive=False)

        view_button = gr.Button("View Ideas")
        view_output = gr.Textbox(label="List of Ideas", interactive=False)

        delete_input = gr.Number(label="Enter idea number to delete", precision=0)
        delete_button = gr.Button("Delete Idea")
        delete_output = gr.Textbox(label="Message", interactive=False)

        add_button.click(add_idea, inputs=idea_input, outputs=add_output)
        view_button.click(view_ideas, outputs=view_output)
        delete_button.click(delete_idea, inputs=delete_input, outputs=delete_output)

    return demo
