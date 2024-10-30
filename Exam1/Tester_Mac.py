import unittest
from io import StringIO
import sys
from contextlib import redirect_stdout

# Import the main function from the user's script
from OpenResponseStudent import main

# Explicitly import unittest.mock
import unittest.mock

class TestActivitySuggestions(unittest.TestCase):
    def setUp(self):
        # Initialize StringIO to capture output
        self.held_output = StringIO()

    def test_sunny_few_participants(self):
        # Set up input
        input_data = ['sunny', '3']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            with redirect_stdout(self.held_output):  # Capture output using redirect_stdout
                main()
        # Check output
        self.assertEqual(self.held_output.getvalue().strip(), "A small group hike would be enjoyable")

    def test_sunny_many_participants(self):
        input_data = ['sunny', '6']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            with redirect_stdout(self.held_output):
                main()
        self.assertEqual(self.held_output.getvalue().strip(), "A team sport like soccer or volleyball at the park.")

    def test_rainy_few_participants(self):
        input_data = ['rainy', '2']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            with redirect_stdout(self.held_output):
                main()
        self.assertEqual(self.held_output.getvalue().strip(), "Board games or a movie indoors would be cozy.")

    def test_rainy_many_participants(self):
        input_data = ['rainy', '7']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            with redirect_stdout(self.held_output):
                main()
        self.assertEqual(self.held_output.getvalue().strip(), "Organize a group indoor trivia or a large board game session.")

if __name__ == '__main__':
    unittest.main()
