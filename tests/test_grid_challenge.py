from _6810110135_.gridChallenge import gridChallenge
import unittest

class gridChallengeTest(unittest.TestCase):
    def test_gridChallenge(self):
        grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
        expected = 'YES'
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected)
    
    def test_gridChallenge_with_unsorted_columns_should_return_NO(self):
        grid = ['abc', 'wxy', 'zab']
        expected = 'NO'
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected)
    
    def test_gridChallenge_with_single_row_should_return_YES(self):
        grid = ['cba']
        expected = 'YES'
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected)
    
    def test_gridChallenge_with_already_sorted_grid_should_return_YES(self):
        grid = ['abc', 'def', 'ghi']
        expected = 'YES'
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected)
    
    def test_gridChallenge_with_empty_grid_should_return_YES(self):
        grid = []
        expected = 'YES'
        
        result = gridChallenge(grid)
        
        self.assertEqual(result, expected)