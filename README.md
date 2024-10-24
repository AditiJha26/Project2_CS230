# Journal App

This is a personal journal app built using Python and Gradio. The app provides four main features to help users manage different types of journal entries: Personal, Goals, Mood Tracker, and Ideas. It includes functionalities like creating, viewing, editing, deleting entries, and managing images for personal journal entries. A security key is required to access the application.

## Features

The app has four main sections:

### 1. Personal Journal

- **Create Entry:** Create personal journal entries with optional image uploads.
- **View Entries:** View all saved entries along with image previews (if any).
- **Search by ID:** Search for a specific entry by its ID.
- **Edit Entry:** Modify the content of an existing entry.
- **Delete Entry:** Remove an entry by its ID.
- **Add Image to Entry:** Upload an image to an existing journal entry.

### 2. Goal Tracker

- **Add Goal:** Set new goals categorized by yearly, monthly, or daily types.
- **View Goals:** Display all existing goals.
- **Edit Goal:** Update an existing goal.
- **Delete Goal:** Remove a goal by its ID.

### 3. Mood Tracker

- **Create Mood Entry:** Log your mood from a predefined list of options and optionally add notes.
- **View Entries:** View a list of all mood entries with their timestamps.
- **Edit Entry:** Update an existing mood entry.
- **Delete Entry:** Remove a mood entry by its ID.

### 4. Ideas

- **Add Idea:** Save a new idea.
- **View Ideas:** Display all saved ideas.
- **Delete Idea:** Remove an idea by its number.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `gradio`
  - `PIL` (Python Imaging Library for handling images)
  - `base64`
  - `json`

You can install the required libraries by running:
pip install gradio pillow

## How to Run the App:

- Clone the repository to your local machine.
- Make sure all the necessary libraries are installed.
- Navigate to the directory containing the project files.
- Run the main.py file to start the Gradio app.
- Once the app is running, open the provided localhost URL (e.g., http://127.0.0.1:7860) in your browser to access the journal app.

## Security Key:

- To Access the app, enter the key: 1234, or you can change to other key as desired in the code.
