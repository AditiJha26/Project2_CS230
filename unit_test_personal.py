# Unit Testing for Personal Tab By Aditi Jha
# Date: October 23, 2024


import unittest
import os
import personal

# Path to the JSON file used for testing 
TEST_FILE_PATH = os.path.join(os.getcwd(), 'test_personal_journal.json')

class TestPersonalJournal(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Setting up the environment before any test runs."""
        # Overriding the FILE_PATH in personal.py to use the test file
        personal.FILE_PATH = TEST_FILE_PATH
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
        """Testing creating a new personal journal entry."""
        result = personal.create_personal_entry("Test Entry 1")
        entries = personal.view_personal_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['content'], "Test Entry 1")
        self.assertIn("Entry 1 created successfully", result)

    def test_view_entries(self):
        """Testing viewing all personal journal entries."""
        personal.create_personal_entry("Entry 1")
        personal.create_personal_entry("Entry 2")
        entries = personal.view_personal_entries()
        self.assertEqual(len(entries), 2)
        self.assertEqual(entries[0]['content'], "Entry 1")
        self.assertEqual(entries[1]['content'], "Entry 2")

    def test_search_entry_by_id(self):
        """Testing searching for a personal journal entry by its ID."""
        personal.create_personal_entry("Entry 1")
        personal.create_personal_entry("Entry 2")
        entry = personal.search_entry_by_id(2)
        self.assertIsNotNone(entry)
        self.assertEqual(entry['content'], "Entry 2")
        self.assertIsNone(personal.search_entry_by_id(3))  # ID that does not exist

    def test_edit_entry(self):
        """Testing editing an existing journal entry."""
        personal.create_personal_entry("Entry 1")
        result = personal.edit_personal_entry(1, "Updated Entry 1")
        entries = personal.view_personal_entries()
        self.assertEqual(entries[0]['content'], "Updated Entry 1")
        self.assertEqual(result, "Entry edited successfully.")

    def test_delete_entry(self):
        """Testing deleting a personal journal entry by its ID."""
        personal.create_personal_entry("Entry 1")
        personal.create_personal_entry("Entry 2")
        result = personal.delete_personal_entry(1)
        entries = personal.view_personal_entries()
        self.assertEqual(len(entries), 1)
        self.assertEqual(entries[0]['id'], 2)
        self.assertEqual(result, "Entry deleted successfully.")

if __name__ == '__main__':
    unittest.main()
