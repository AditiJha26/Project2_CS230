# Unit testing for Moodtracker tab by Sumeyya Sherief 

import unittest
import os
import moodtracker  

# Path to the JSON file used for testing
TEST_FILE_PATH = os.path.join(os.getcwd(), 'test_mood_tracker.json')

class TestMoodTracker(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setting up the environment before any test runs."""
        # Overriding the FILE_PATH in mood_tracker.py to use the test file
        moodtracker.FILE_PATH = TEST_FILE_PATH
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)  # Ensuring fresh start

    @classmethod
    def tearDownClass(cls):
        """Cleaning up after all tests are done."""
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)  # Cleaning up the test file

    def setUp(self):
        """Resetting the test file before each test."""
        if os.path.exists(TEST_FILE_PATH):
            os.remove(TEST_FILE_PATH)

    def test_create_entry(self):
        """Testing creating a new mood entry."""
        result = moodtracker.create_mood_entry("Happy", "Feeling great today!")
        entries = moodtracker.load_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['mood'], "Happy")
        self.assertIn("Mood entry saved with ID:", result)

    def test_view_entries(self):
        """Testing viewing all mood entries."""
        moodtracker.create_mood_entry("Happy", "Feeling great!")
        moodtracker.create_mood_entry("Sad", "Not my best day.")
        entries = moodtracker.view_mood_entries()
        self.assertIn("Happy", entries)
        self.assertIn("Sad", entries)

    def test_edit_entry(self):
        """Testing editing an existing mood entry."""
        moodtracker.create_mood_entry("Happy", "Feeling great!")
        result = moodtracker.edit_mood_entry(1, "Excited", "Can't wait for the weekend!")
        entries = moodtracker.load_entries()
        self.assertEqual(entries[0]['mood'], "Excited")
        self.assertEqual(entries[0]['notes'], "Can't wait for the weekend!")
        self.assertEqual(result, "Entry edited successfully.")

    def test_delete_entry(self):
        """Testing deleting a mood entry by its ID."""
        moodtracker.create_mood_entry("Happy", "Feeling great!")
        moodtracker.create_mood_entry("Sad", "Not my best day.")
        result = moodtracker.delete_mood_entry(1)
        entries = moodtracker.load_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['mood'], "Sad")
        self.assertEqual(result, "Entry deleted successfully.")

    def test_search_entry_by_id(self):
        """Testing searching for a mood entry by its ID."""
        moodtracker.create_mood_entry("Entry 1", "Feeling fine.")
        moodtracker.create_mood_entry("Entry 2", "Feeling tired.")
        entry = moodtracker.load_entries()[1]  # Get the second entry
        self.assertEqual(entry['mood'], "Entry 2")
        self.assertEqual(entry['notes'], "Feeling tired.")
        # Test with a non-existing ID
        #self.assertIsNone(moodtracker.search_entry_by_id(3))  # Assuming this function exists

if __name__ == '__main__':
    unittest.main()
