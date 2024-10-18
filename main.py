import personal
import datetime

from Goals import Goal, GoalTracker

def show_personal_menu():

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
            personal.create_personal_entry(content)
        elif choice == '2':
            personal.view_personal_entries()
        elif choice == '3':
            old_content = input("Enter the content you want to edit: ")
            new_content = input("Enter the new content: ")
            personal.edit_personal_entry(old_content, new_content)
        elif choice == '4':
            content = input("Enter the content of the entry you want to delete: ")
            personal.delete_personal_entry(content)
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

def show_main_menu():
    """Display the main menu for the journal app. ~ Aditi ~ 10/07/2024"""
    tracker = GoalTracker()
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
