import datetime 

class Goal: 
    def __init__ (self, description, goal_type, date_created):
        self.description = description 
        self.goal_type = goal_type 
        self.date_created = date_created
        self.completed = False

class GoalTracker:
    def __init__(self):
        self.goals = []

    def add_goals(self, goal):
        self.goals.append(goal)

    def view_goals(self):
        for i , goal in enumerate(self.goals, 1):
            status = "Completed" if goal.completed else "In progress"
            print(f"{i}.[{status}] {goal.goal_type} Goal: {goal.description} (Created: {goal.date_created})")

    def complete_goal(self, index):
        if 1 <= index <= len(self.goals):
            self.goals[index - 1].completed = True
            print("Goal marked as complete")
        else:
            print("Invalid goal number")

def main():
    tracker = GoalTracker()
    while True:
        print ("\n Goal Tracker")
        print("1. Set a new goal")
        print("2. View goals")
        print("3. Mark goal as completed ")
        print("4. Exit")

        choice = input("Please enter a number between (1-4): ")

        if choice == '1':
            goal_type = input("Enter goal type (yearly/monthly/daily):").lower()
            
            if goal_type not in ['yearly', 'monthly', 'daily']:
                print("Invalid input. Please try again.")

                continue
            description = input("Enter you goal: ")
            date_created = datetime.date.today().strftime("%Y-%m-%d")
            new_goal = Goal(description, goal_type, date_created)
            tracker.add_goals(new_goal)
            print("Goal added successfully!")

        elif choice =='2':
            tracker.view_goals()

        elif choice == '3':
            tracker.view_goals()
            index = int(input("Enter the number of the goal to mark as complete: "))
            tracker.complete_goal(index)
        elif choice == '4':
            print("Exit")
        
            break

        else:
             print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() 
        

