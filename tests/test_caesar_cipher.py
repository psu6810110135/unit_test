from _6810110135_.caesarCipher import caesarCipher
import unittest


class caesarCipherTest(unittest.TestCase):
    def test_middle_out_should_return_okffng_owvb(self):
        self.assertEqual(caesarCipher("middle-0utz", 2), "okffng-0wvb")
    
    def test_hello_world_should_return_khoor_zruog(self):
        self.assertEqual(caesarCipher("hello-world", 3), "khoor-zruog")
    
    def test_all_lowercase_should_rotate_with_wrap_around(self):
        self.assertEqual(caesarCipher("xyz", 3), "abc")
    
    def test_mixed_case_should_preserve_case(self):
        self.assertEqual(caesarCipher("abc", 1), "bcd")
    
    def test_empty_string_should_return_empty(self):
        self.assertEqual(caesarCipher("", 5), "")
        