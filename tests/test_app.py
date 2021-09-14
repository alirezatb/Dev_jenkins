import unittest
from app import remove_no_pattern


class Testapp(unittest.TestCase):
    def test_remove_no_pattern(self):
        get_value = remove_no_pattern()
        self.assertEqual(get_value, 12)


