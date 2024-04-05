import unittest
import os
from main import find_popular_words

class TestCountWords(unittest.TestCase):

    def test_count_words(self):
        test_file_path = 'test_data.txt'
        with open(test_file_path, 'w') as file:
            file.write("apple orange banana apple orange grapefruit")

        expected_result = {'apple': 2, 'orange': 2, 'banana': 1, 'grapefruit': 1}
        result = find_popular_words(test_file_path)
        os.remove(test_file_path)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
