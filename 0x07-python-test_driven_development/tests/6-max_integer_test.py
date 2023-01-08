#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Checks the list for maximum number """

    def test_max_beginning(self):
        """Test a list for maximum value at the beginning"""
        sample = [9, 3, 7, 1, 5]
        self.assertEqual(max_integer(sample), 9)

    def test_max_middle(self):
        """Test a list for maximum value at the middle"""
        sample = [3, 7, 9, 1, 5]
        self.assertEqual(max_integer(sample), 9)

    def test_max_end(self):
        """Test a list for maximum value at end"""
        sample = [1, 3, 5, 7, 9]
        self.assertEqual(max_integer(sample), 9)

    def test_max_one_negative(self):
        """Test a list with a single negative number for maximum value"""
        sample = [1, 3, -9, 7, 9]
        self.assertEqual(max_integer(sample), 9)

    def test_max_all_negative(self):
        """Test a list with all negative number for maximum value"""
        sample = [-1, -3, -5, -7, -9]
        self.assertEqual(max_integer(sample), -1)

    def test_max_one_number(self):
        """Test a list containing one number for maximum value"""
        sample = [9]
        self.assertEqual(max_integer(sample), 9)

    def test_max_empty(self):
        """Test an empty list for maximum value"""
        sample = []
        self.assertEqual(max_integer(sample), None)
