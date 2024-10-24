# Mastewal
import unittest
import os
from datetime import date
import goal
from goal import GoalTracker
TEST_FILE_PATH = os.path.join(os.getcwd(), 'test_goals.json')

class TestGoalTracker(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        goal.GOALS_FILE = TEST_FILE_PATH
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def setUp(self):
        self.tracker = GoalTracker() 
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def test_add_goal(self):
        result = self.tracker.add_goals("Learn Python", "monthly") 
        self.assertIn("Goal added successfully", result)
        self.assertEqual(len(self.tracker.goals), 1)
        self.assertEqual(self.tracker.goals[0].description, "Learn Python")
        self.assertEqual(self.tracker.goals[0].goal_type, "monthly")
        self.assertEqual(self.tracker.goals[0].date_created, date.today().strftime("%Y-%m-%d"))

    def test_view_goals(self):
        self.tracker.add_goals("Learn Python", "monthly")
        goals_string = self.tracker.view_goals_as_string()
        self.assertIn("ID: 1", goals_string)
        

    def test_delete_goal(self):
        self.tracker.add_goals("Learn Python", "monthly")
        result = self.tracker.delete_goal(1)
        self.assertIn("deleted", result)
        self.assertEqual(len(self.tracker.goals), 1)
        
    def test_edit_goal(self):
        self.tracker.add_goals("Learn Python", "monthly")
        result = self.tracker.edit_goal(1, "Master Python", "yearly")
    
        self.assertEqual(result, "Goal (ID: 1) has been updated.")
    
        
        self.assertEqual(self.tracker.goals[0].description, "Master Python")
        self.assertEqual(self.tracker.goals[0].goal_type, "yearly")


    


if __name__ == '__main__':
    unittest.main()
