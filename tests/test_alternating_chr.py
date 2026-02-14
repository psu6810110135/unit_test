from _6810110135_.alternatingChr import alternatingCharacters
import unittest

class alternatingChr(unittest.TestCase):
    def test_AAAA_should_return_3(self):
        self.assertEqual(alternatingCharacters("AAAA"), 3)
    def test_BBBBB_should_return_0(self):
        self.assertEqual(alternatingCharacters("BBBBB"), 4)
    def test_ABABABAB_should_return_1(self):
        self.assertEqual(alternatingCharacters("ABABABAB"), 0)
    def test_BABABA_should_return_2(self):
        self.assertEqual(alternatingCharacters("BABABA"), 0)
    def test_AAABBB_should_return_1(self):
        self.assertEqual(alternatingCharacters("AAABBB"), 4)