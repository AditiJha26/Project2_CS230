import personal
import moodtracker
import datetime
import gradio as gr

from Goals import Goal, GoalTracker

def show_personal_menu():
<<<<<<< HEAD

=======
    """Displaying the Personal journal menu and handle user input - Aditi - 10/14/2024"""
>>>>>>> a892ff5678bfc8cfc3088a5f19201f26ccd7bc40
    while True:
        print("\nPersonal Journal Menu")
        print("1. Create a new entry")
        print("2. View all entries")
        print("3. Edit an entry")
        print("4. Delete an entry")
        print("5. Go back")
        choice = input("Enter your choice: ")

        if choice == '1':
            content = input("Enter your personal journal entry: ")
            image_path = input("Enter the path to your image (or leave blank): ")
            image_path = image_path if image_path else None
            personal.create_personal_entry(content, image_path)
        elif choice == '2':
            personal.view_personal_entries()
        elif choice == '3':
            try:
                entry_id = int(input("Enter the ID of the entry you want to edit: "))
                new_content = input("Enter the new content: ")
                personal.edit_personal_entry(entry_id, new_content)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        elif choice == '4':
            try:
                entry_id = int(input("Enter the ID of the entry you want to delete: "))
                personal.delete_personal_entry(entry_id)
            except ValueError:
                print("Invalid ID. Please enter a valid number.")
        elif choice == '5':
            print("Returning to main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

def show_goal_tracker_menu(tracker):
    while True:
        print("\nGoal Tracker")
        print("1. Set a new goal")
        print("2. View goals")
        print("3. Mark goal as completed")
        print("4. Delete a goal")
        print("5. Go back")

        choice = input("Enter your choice: ")

        if choice == '1':
            goal_type = input("Enter goal type (yearly/monthly/daily): ").lower()
            
            if goal_type not in ['yearly', 'monthly', 'daily']:
                print("Invalid input. Please try again.")
                continue
            description = input("Enter your goal: ")
            date_created = datetime.date.today().strftime("%Y-%m-%d")
            new_goal = Goal(description, goal_type, date_created)
            tracker.add_goals(new_goal)
            print("Goal added successfully!")

        elif choice == '2':
            tracker.view_goals()

        elif choice == '3':
            tracker.view_goals()
            try:
                index = int(input("Enter the number of the goal to mark as complete: "))
                tracker.complete_goal(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice =='4':
            tracker.view_goals()
            try:
                index = int(input("Enter the number of the goal to delete:"))
                tracker.delete_goal(index)
            except ValueError:
                print("Invalid input. Please enter a number.")

        elif choice == '5':
            print("Returning to main menu...")
            break

        else:
            print("Invalid choice. Please try again.")

def mood_interface():
    with gr.Blocks() as app:
        gr.Markdown("# Mood Tracker")

       
        mood_options = ["Happy", "Sad", "Excited", "Stressed", "Calm", "Anxious", "Angry", "Relaxed"]

       
        with gr.Tab("Create Entry"):
            mood_input = gr.Radio(label="Select Your Mood", choices=mood_options)
            notes_input = gr.Textbox(label="Notes (Optional)", lines=3)
            create_button = gr.Button("Create Mood Entry")
            create_output = gr.Textbox(label="Message")
            create_button.click(fn=create_mood_entry, inputs=[mood_input, notes_input], outputs=create_output)

        
        with gr.Tab("View Entries"):
            view_button = gr.Button("View All Entries")
            view_output = gr.Textbox(label="All Mood Entries", lines=10)
            view_button.click(fn=view_mood_entries, outputs=view_output)

            gr.Markdown("### Edit or Delete an Entry")

            entry_id_input = gr.Number(label="Entry ID", value=None)

         
            new_mood_input = gr.Radio(label="New Mood", choices=mood_options)
            new_notes_input = gr.Textbox(label="New Notes (Optional)", lines=3)
            edit_button = gr.Button("Edit Mood Entry")
            edit_output = gr.Textbox(label="Edit Message")
            edit_button.click(fn=edit_mood_entry, inputs=[entry_id_input, new_mood_input, new_notes_input], outputs=edit_output)

            
            delete_button = gr.Button("Delete Mood Entry")
            delete_output = gr.Textbox(label="Delete Message")
            delete_button.click(fn=delete_mood_entry, inputs=[entry_id_input], outputs=delete_output)

    return app

# Launch Gradio app
mood_interface().launch()

def show_main_menu():
<<<<<<< HEAD
    """Display the main menu for the journal app. ~ Aditi ~ 10/07/2024"""
    tracker = GoalTracker()
=======
    """Displaying the main menu for the journal app - Aditi - 10/14/2024"""
>>>>>>> a892ff5678bfc8cfc3088a5f19201f26ccd7bc40
    while True:
        print("\nMain Menu")
        print("1. Personal Journal")
        print("2. Goal")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_personal_menu()
        elif choice =='2':
            show_goal_tracker_menu(tracker) 
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



if __name__ == "__main__":
    show_main_menu()
