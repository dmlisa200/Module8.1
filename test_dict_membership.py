import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict_membership.in_dict('pres', 'Sara'), True)


class TestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(dict_membership.in_dict('VP', 'Jan'), False)


if __name__ == '__main__':
    unittest.main()
