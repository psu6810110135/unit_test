from _6810110135_.cat_and_mouse import cat_and_mouse
import unittest

class CatAndMouseTest(unittest.TestCase):
    def test_cat_and_mouse(self):
        pos = '1 2 3'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Cat B')
    def test_cat_and_mouse_2(self):
        pos = '1 3 2'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Mouse C')
    def test_cat_and_mouse_3(self):
        pos = '2 1 3'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Cat A')
    def test_cat_and_mouse_4(self):
        pos = '1 1 1'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Mouse C')
    def test_cat_and_mouse_5(self):
        pos = '1 2 2'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Cat B')
    def test_cat_and_mouse_6(self):
        pos = '2 2 1'
        res = cat_and_mouse(*map(int, pos.split()))
        self.assertEqual(res, 'Mouse C')