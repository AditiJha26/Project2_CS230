# Unit Testing by Rebecca R.

import unittest
import os
import json
import Ideas

TEST_FILE_PATH = os.path.join(os.getcwd(), 'test_Ideas.json')

class TestIdeas(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        Ideas.GOALS_FILE = TEST_FILE_PATH
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)
    
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def setUp(self):
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def test_load_ideas_empty(self):
        self.assertEqual(load_ideas(), [], "Should return an empty list when file is empty")

    def test_save_and_load_ideas(self):
        ideas = ["Idea 1", "Idea 2"]
        save_ideas(ideas)
        self.assertEqual(load_ideas(), ideas, "Should return saved ideas from file")

    def test_view_ideas_empty(self):
        self.assertEqual(view_ideas(), "No ideas found.", "Should return 'No ideas found.' when there are no ideas")

    def test_view_ideas_with_content(self):
        ideas = ["Idea 1", "Idea 2"]
        save_ideas(ideas)
        self.assertEqual(view_ideas(), "1. Idea 1\n2. Idea 2", "Should return formatted list of ideas")

    def test_add_idea_empty_string(self):
        self.assertEqual(add_idea(""), "Idea cannot be empty.", "Should return error message when adding empty idea")

    def test_add_idea(self):
        add_idea("New Idea")
        self.assertIn("New Idea", load_ideas(), "The added idea should be in the saved ideas list")

    def test_delete_idea_valid_index(self):
        ideas = ["Idea 1", "Idea 2", "Idea 3"]
        save_ideas(ideas)
        self.assertEqual(delete_idea(2), "Idea 'Idea 2' deleted successfully.", "Should delete idea at index 2")
        self.assertEqual(load_ideas(), ["Idea 1", "Idea 3"], "Should update list correctly after deletion")

    def test_delete_idea_invalid_index(self):
        ideas = ["Idea 1"]
        save_ideas(ideas)
        self.assertEqual(delete_idea(5), "Invalid idea number.", "Should return error for invalid index")

    def test_delete_idea_non_integer_index(self):
        ideas = ["Idea 1"]
        save_ideas(ideas)
        self.assertEqual(delete_idea("a"), "Invalid input. Please enter a valid number.", "Should return error for non-integer index")


if __name__ == '__main__':
    unittest.main()
