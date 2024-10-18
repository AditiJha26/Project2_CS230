# Author: Mastewal Berhe
# 10/12/2024
import json

class Goal: 
    def __init__(self, description, goal_type, date_created, completed=False):
        self.description = description 
        self.goal_type = goal_type 
        self.date_created = date_created
        self.completed = completed

    def to_dict(self):
        return {
            "description": self.description,
            "goal_type": self.goal_type,
            "date_created": self.date_created,
            "completed": self.completed
            
        }

class GoalTracker:
    def __init__(self):
        self.goals = self.load_goals()

    def load_goals(self):
        try:
            with open("goals.json", "r") as f:
                goals_data = json.load(f)
                return [Goal(**goal) for goal in goals_data]
        except FileNotFoundError:
            return []
        
    def save_goals(self):
        with open("goals.json", "w") as f:
            json.dump([goal.to_dict() for goal in self.goals], f, indent=2)

    def add_goals(self, goal):
        self.goals.append(goal)
        self.save_goals()

    def view_goals(self):
        if not self.goals:
            print("No goals set yet.")
        else:
            for i, goal in enumerate(self.goals, 1):
                status = "Completed" if goal.completed else "In progress"
                print(f"{i}. [{status}] {goal.goal_type.capitalize()} Goal: {goal.description} (Created: {goal.date_created})")

    def complete_goal(self, index):
        if 1 <= index <= len(self.goals):
            self.goals[index - 1].completed = True
            self.save_goals()
            print("Goal marked as complete")
        else:
            print("Invalid goal number")

    def delete_goal(self, index):
        if 1 <= index <= len(self.goals):
            deleted_goal = self.goals.pop(index -1 )
            self.save_goals()
            print(f"Goal '{deleted_goal.description}' has been deleted.")

        else:
            print("Invalid goal number.")