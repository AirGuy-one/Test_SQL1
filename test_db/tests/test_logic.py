from unittest import TestCase
from test_db.logic import function


class LogicTestCase(TestCase):
    def test_plus(self):
        result = function(6, 13, "+")
        self.assertEqual(19, result)

    def test_minus(self):
        result = function(6, 13, '-')
        self.assertEqual(-7, result)

    def test_empty(self):
        result = function(6, 13, 'some')
        self.assertEqual(None, result)



