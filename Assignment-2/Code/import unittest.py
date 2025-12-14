import unittest
from _2021080_q3 import read_yearbook_file

class TestReadYearbookFile(unittest.TestCase):
    
    def test_read_valid_yearbook_file(self):
        # Create a sample yearbook file
        with open('test_yearbook.txt', 'w') as f:
            f.write("Alice:\nBob, 1\nCharlie, 1\nDavid, 0\n")
            f.write("Bob:\nAlice, 1\nCharlie, 0\nDavid, 1\n")
            f.write("Charlie:\nAlice, 1\nBob, 1\nDavid, 1\n")
            f.write("David:\nAlice, 0\nBob, 0\nCharlie, 0\n")
        
        expected_yearbook = {
            'Alice': {'Bob': 1, 'Charlie': 1, 'David': 0},
            'Bob': {'Alice': 1, 'Charlie': 0, 'David': 1},
            'Charlie': {'Alice': 1, 'Bob': 1, 'David': 1},
            'David': {'Alice': 0, 'Bob': 0, 'Charlie': 0}
        }
        
        result = read_yearbook_file('test_yearbook.txt')
        self.assertEqual(result, expected_yearbook)
    
    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_yearbook_file('nonexistent_file.txt')

if __name__ == '__main__':
    unittest.main()