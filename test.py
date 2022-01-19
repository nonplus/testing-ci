import unittest
from main import respond

class TestIsOdd(unittest.TestCase):

    def test_ask_name(self):
        self.assertEqual(respond("What is your name?"), "My name is chatbot! What's yours?")

    def test_dont_understand(self):
      self.assertEqual(respond("Blah?"), "Sorry I did not understand that.")

if __name__ == '__main__':
    unittest.main()