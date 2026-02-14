import unittest
from _6810110135_.funny_str import funnyString

class TestFunny(unittest.TestCase):
    def test_funny_case(self):
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny_case(self):
        self.assertEqual(funnyString("bcxz"), "Not Funny")
    
    def test_single_char(self):
        self.assertEqual(funnyString("a"), "Funny")
        
    def test_empty_string(self):
        self.assertEqual(funnyString(""), "Funny")
        
    def test_long_string(self):
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyz"), "Funny")