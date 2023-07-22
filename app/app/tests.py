"""
Sample test file
"""

from django.test import SimpleTestCase

from . import calc


class CalcTest(SimpleTestCase):
    '''Test module for calc.py'''

    def test_add_numbers(self):
        '''Test add function'''
        res = calc.add(3, 8)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        '''Test subtract function'''
        res = calc.subtract(3, 8)
        self.assertEqual(res, -5)
