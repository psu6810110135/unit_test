from _6810110135_.alternate import alternate
import unittest

class alternateTest(unittest.TestCase):
    def test_alternate_should_return_1(self):
        self.assertEqual(alternate("beabeefeab"), 5)
    
    def test_all_same_char_should_return_0(self):
        self.assertEqual(alternate("aaaa"), 0)
    
    def test_already_alternating_should_return_full_length(self):
        self.assertEqual(alternate("ababab"), 6)
    
    def test_three_chars_should_find_best_pair(self):
        self.assertEqual(alternate("abcabc"), 4)
    
    def test_empty_string_should_return_0(self):
        self.assertEqual(alternate(""), 0)