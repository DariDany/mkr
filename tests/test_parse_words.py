import unittest
from unittest.mock import patch
from main import find_popular_words

class TestFindPopularWords(unittest.TestCase):

    @patch('builtins.open', unittest.mock.mock_open(read_data='Alice has a cat and a dog.'))
    def test_find_popular_words(self):
        expected_result = {'a': 2, 'alice': 1, 'has': 1, 'cat': 1, 'and': 1, 'dog': 1}
        result = find_popular_words('dummy/path')
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()