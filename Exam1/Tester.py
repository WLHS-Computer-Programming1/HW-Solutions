import unittest
from io import StringIO
import sys

# Import the main function from the user's script
from OpenResponseStudent import main  # replace 'your_script' with the name of your file (without .py)

class TestActivitySuggestions(unittest.TestCase):
    def setUp(self):
        # Redirect stdout to capture print statements
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        # Reset stdout
        sys.stdout = sys.__stdout__

    def test_sunny_few_participants(self):
        # Set up input
        input_data = ['sunny', '3']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            main()
        # Check output
        self.assertEqual(self.held_output.getvalue().strip(), "A small group hike would be enjoyable")

    def test_sunny_many_participants(self):
        input_data = ['sunny', '6']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            main()
        self.assertEqual(self.held_output.getvalue().strip(), "A team sport like soccer or volleyball at the park.")

    def test_rainy_few_participants(self):
        input_data = ['rainy', '2']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            main()
        self.assertEqual(self.held_output.getvalue().strip(), "Board games or a movie indoors would be cozy.")

    def test_rainy_many_participants(self):
        input_data = ['rainy', '7']
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            main()
        self.assertEqual(self.held_output.getvalue().strip(), "Organize a group indoor trivia or a large board game session.")

if __name__ == '__main__':
    unittest.main()
