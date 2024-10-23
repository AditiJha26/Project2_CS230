# Author: Aditi Jha
# October 23, 2024: Combined all code to get one main (starter) file. Added corrected gradio interface, added security pin, added starting menu options. 

import gradio as gr
import personal
import goal
import moodtracker
import ideas
import os
import base64

# Security key for accessing the app
SECURITY_KEY = "1234"

def check_security_key(input_key):
    """Check if the entered security key is correct."""
    if input_key == SECURITY_KEY:
        return gr.update(visible=True), gr.update(visible=False)  # Show the app and hide the login
    else:
        return gr.update(visible=False), gr.update(visible=True, value="Incorrect key. Try again.")
    
def create_entry_interface(content, image_file):
    """Gradio interface for creating a new entry."""
    image_data = None
    if image_file is not None:
        # Handle Gradio's file object by accessing the file path
        image_path = image_file.name  # Get the uploaded file's name
        with open(image_path, 'rb') as img_file:  # Open the file and read it as binary
            image_data = base64.b64encode(img_file.read()).decode('utf-8')  # Read the file content and encode to base64

    return personal.create_personal_entry(content, image_data)


def view_entries_interface():
    """Gradio interface for viewing all entries."""
    entries = personal.view_personal_entries()
    if not entries:
        return "No entries found.", []
    
    # Generate display text and collect image paths
    display_text = ""
    image_paths = []
    for entry in entries:
        display_text += f"ID: {entry['id']}\nTimestamp: {entry['timestamp']}\nContent: {entry['content']}\n"
        if entry.get('image_path'):
            image_paths.append(entry['image_path'])  # Append the image path directly
        else:
            display_text += "No Image\n"
        display_text += "-" * 40 + "\n"
    
    return display_text, image_paths  # Return the paths for the gallery

def search_entry_by_id(entry_id):
    """Gradio interface to search for an entry by its ID."""
    entry = personal.search_entry_by_id(int(entry_id))  # Get the entry by ID
    if entry:
        entry_text = f"ID: {entry['id']}\nTimestamp: {entry['timestamp']}\nContent: {entry['content']}\n"
        image_paths = [entry['image_path']] if entry.get('image_path') else []
        return entry_text, image_paths
    else:
        return "Entry not found.", []

def edit_entry_interface(entry_id, new_content):
    """Gradio interface for editing an entry by ID."""
    return personal.edit_personal_entry(entry_id, new_content)

def delete_entry_interface(entry_id):
    """Gradio interface for deleting an entry by ID."""
    return personal.delete_personal_entry(entry_id)

def add_image_interface(entry_id, image_file):
    """Gradio interface for adding an image to an entry by ID."""
    try:
        entry_id = int(entry_id)  # Ensure ID is an integer
        if image_file is None:
            return "No image uploaded."
        
        # Convert the uploaded file to base64
        image_path = image_file.name  # Get the uploaded file's name
        with open(image_path, 'rb') as img_file:
            image_data = base64.b64encode(img_file.read()).decode('utf-8')  # Read and encode file content
        
        result = personal.add_image_to_entry(entry_id, image_data)
        return result
    except ValueError:
        return "Invalid ID. Please enter a valid number."
    except Exception as e:
        return f"Failed to process the image: {str(e)}"

# Personal Journal tab
def personal_tab():
    with gr.Blocks() as personal_interface:
        gr.Markdown("## Personal Journal")
        with gr.Tab("Create Entry"):
            content = gr.Textbox(label="Enter your personal journal entry:")
            image_file = gr.File(label="Upload Image File")
            create_button = gr.Button("Create Entry")
            create_result = gr.Textbox()
            create_button.click(create_entry_interface, inputs=[content, image_file], outputs=create_result)
        with gr.Tab("View Entries"):
            view_button = gr.Button("View Entries")
            view_text = gr.Textbox(label="Entry Details")  # For displaying the text details
            view_images = gr.Gallery(label="Image Previews")  # Gallery for displaying image previews
            view_button.click(view_entries_interface, outputs=[view_text, view_images])
        with gr.Tab("Search by ID"):
            entry_id_search = gr.Textbox(label="Enter the ID of the entry to search:")
            search_button = gr.Button("Search Entry")
            search_text = gr.Textbox(label="Search Result")
            search_images = gr.Gallery(label="Search Image Preview")
            search_button.click(search_entry_by_id, inputs=[entry_id_search], outputs=[search_text, search_images])
        with gr.Tab("Edit Entry"):
            entry_id_edit = gr.Textbox(label="Enter the ID of the entry you want to edit:")
            new_content = gr.Textbox(label="Enter the new content:")
            edit_button = gr.Button("Edit Entry")
            edit_result = gr.Textbox()
            edit_button.click(edit_entry_interface, inputs=[entry_id_edit, new_content], outputs=edit_result)
        with gr.Tab("Delete Entry"):
            entry_id_delete = gr.Textbox(label="Enter the ID of the entry you want to delete:")
            delete_button = gr.Button("Delete Entry")
            delete_result = gr.Textbox()
            delete_button.click(delete_entry_interface, inputs=[entry_id_delete], outputs=delete_result)
        with gr.Tab("Add Image to Entry"):
            entry_id_image = gr.Textbox(label="Enter the ID of the entry you want to add an image to:")
            image_file = gr.File(label="Upload Image File")
            image_button = gr.Button("Add Image")
            image_result = gr.Textbox()
            image_button.click(add_image_interface, inputs=[entry_id_image, image_file], outputs=image_result)
    return personal_interface

# Goal Tracker tab
def goal_tab():
    return goal.Goal_interface()

# Mood Tracker tab
def mood_tracker_tab():
    return moodtracker.mood_interface()

# Ideas tab
def ideas_tab():
    return ideas.ideas_interface()

def main_interface():
    with gr.Blocks() as demo:
        # Add a security key input before accessing the app
        security_key_input = gr.Textbox(label="Enter security key:", type="password")
        login_button = gr.Button("Login")
        error_message = gr.Textbox(visible=False)
        
        # Main app will be hidden initially until the correct key is entered
        with gr.Group(visible=False) as journal_app:
            gr.Markdown("## Journal App - Choose a Section")
            with gr.Tabs():
                with gr.TabItem("Personal"):
                    personal_tab()  # Ensure it is called to load content
                with gr.TabItem("Goal Tracker"):
                    goal_tab()  # Ensure it is called to load content
                with gr.TabItem("Mood Tracker"):
                    mood_tracker_tab()  # Ensure it is called to load content
                with gr.TabItem("Ideas"):
                    ideas_tab()  # Ensure it is called to load content

        # Link login button to check security key
        login_button.click(check_security_key, inputs=[security_key_input], outputs=[journal_app, error_message])

    demo.launch()

if __name__ == "__main__":
    main_interface()


