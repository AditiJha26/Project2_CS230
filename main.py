import personal

def show_personal_menu():
    """Display the Personal journal menu and handle user input. ~ Aditi ~ 10/07/2024"""
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

def show_main_menu():
    """Display the main menu for the journal app. ~ Aditi ~ 10/07/2024"""
    while True:
        print("\nMain Menu")
        print("1. Personal Journal")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            show_personal_menu()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    show_main_menu()
