# Author: Mastewal Berhe
# Updated by Aditi (adding ID functionality)

import json
import gradio as gr
import datetime
import os


GOALS_FILE = os.path.join(os.getcwd(), 'goals.json')  
class Goal:
    def __init__(self, goal_id, description, goal_type, date_created, completed=False):
        self.goal_id = goal_id
        self.description = description
        self.goal_type = goal_type
        self.date_created = date_created

    def to_dict(self):
        return {
            "goal_id": self.goal_id,
            "description": self.description,
            "goal_type": self.goal_type,
            "date_created": self.date_created,
        }

class GoalTracker:
    def __init__(self):
        self.goals = self.load_goals()

    def load_goals(self):
        try:
            with open("goals.json", "r") as f:
                goals_data = json.load(f)
                goals = []
                for goal in goals_data:
                    # Assigning a new goal_id if it's missing from old entries
                    if "goal_id" not in goal:
                        goal["goal_id"] = generate_new_id(goals)  # Passing the current goals to generate a new ID
                    goals.append(Goal(**goal))
                return goals
        except FileNotFoundError:
            return []

    def save_goals(self):
        with open("goals.json", "w") as f:
            json.dump([goal.to_dict() for goal in self.goals], f, indent=2)

    def add_goals(self, description, goal_type):
        new_id = generate_new_id(self.goals)  # Passing the current list of goals to generate a new ID
        date_created = datetime.date.today().strftime("%Y-%m-%d")
        new_goal = Goal(goal_id=new_id, description=description, goal_type=goal_type, date_created=date_created)
        self.goals.append(new_goal)
        self.save_goals()
        return f"Goal added successfully: {description} ({goal_type})"

    def view_goals_as_string(self):
        if not self.goals:
            return "No goals set yet."
        else:
            result = ""
            for goal in self.goals:
                # Safeguard against missing or None goal_type
                goal_type = goal.goal_type if goal.goal_type else "Unknown"
                result += f"ID: {goal.goal_id} | {goal_type.capitalize()} Goal: {goal.description} (Created: {goal.date_created})\n"
            return result

    def delete_goal(self, goal_id):
        for i, goal in enumerate(self.goals):
            if goal.goal_id == int(goal_id):
                deleted_goal = self.goals.pop(i)
                self.save_goals()
                return f"Goal '{deleted_goal.description}' (ID: {goal_id}) has been deleted."
        return "Invalid goal ID."


# Moving this function outside the class
def generate_new_id(goals):
    if goals:
        return max(goal.goal_id for goal in goals) + 1
    else:
        return 1


# Modified Goal interface function, by Aditi
def add_goal_interface(goal_type, description):
    tracker = GoalTracker()
    return tracker.add_goals(description, goal_type)


def Goal_interface():
    tracker = GoalTracker()
    with gr.Blocks() as demo:
        gr.Markdown("# Goal Tracker")

        with gr.Tab("Add Goal"):
            goal_type = gr.Dropdown(["yearly", "monthly", "daily"], label="Goal Type")
            description = gr.Textbox(label="Goal description")
            add_button = gr.Button("Add Goal")
            add_output = gr.Textbox(label="Result")
            add_button.click(add_goal_interface, inputs=[goal_type, description], outputs=add_output)

        with gr.Tab("View Goals"):
            view_button = gr.Button("View Goals")
            view_output = gr.Textbox(label="Goals", lines=10)
            view_button.click(tracker.view_goals_as_string, outputs=view_output)

        with gr.Tab("Delete Goal"):
            delete_index = gr.Textbox(label="Enter Goal ID to Delete")
            delete_button = gr.Button("Delete Goal")
            delete_output = gr.Textbox(label="Result")
            delete_button.click(tracker.delete_goal, inputs=delete_index, outputs=delete_output)

    return demo
