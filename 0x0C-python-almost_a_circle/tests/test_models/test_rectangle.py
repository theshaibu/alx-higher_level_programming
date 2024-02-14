#!/usr/bin/python3
# test_rectangle.py
"""Defines unittests for models/rectangle.py.

Unittest classes:
    TestRectangleInstantiation - Tests for instantiation of the Rectangle class.
    TestRectangleWidth - Tests for initialization of Rectangle width attribute.
    TestRectangleHeight - Tests for initialization of Rectangle height attribute.
    TestRectangleX - Tests for initialization of Rectangle x attribute.
    TestRectangleY - Tests for initialization of Rectangle y attribute.
    TestRectangleOrderOfInitialization - Tests for the order of attribute initialization.
    TestRectangleArea - Tests for the area method of the Rectangle class.
    TestRectangleStdout - Tests for __str__ and display methods of Rectangle class.
    TestRectangleUpdateArgs - Tests for the update_args method of the Rectangle class.
    TestRectangleUpdateKwargs - Tests for the update_kwargs method of the Rectangle class.
"""
import io
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInstantiation(unittest.TestCase):
    """Tests for instantiation of the Rectangle class."""

    def test_rectangle_is_base(self):
        self.assertIsInstance(Rectangle(10, 2), Base)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Rectangle()

    # ... (rest of the test methods remain the same)

class TestRectangleWidth(unittest.TestCase):
    """Tests for initialization of Rectangle width attribute."""

    # ... (rest of the test methods remain the same)

class TestRectangleHeight(unittest.TestCase):
    """Tests for initialization of Rectangle height attribute."""

    # ... (rest of the test methods remain the same)

class TestRectangleX(unittest.TestCase):
    """Tests for initialization of Rectangle x attribute."""

    # ... (rest of the test methods remain the same)

class TestRectangleY(unittest.TestCase):
    """Tests for initialization of Rectangle y attribute."""

    # ... (rest of the test methods remain the same)

class TestRectangleOrderOfInitialization(unittest.TestCase):
    """Tests for the order of attribute initialization."""

    # ... (rest of the test methods remain the same)

class TestRectangleArea(unittest.TestCase):
    """Tests for the area method of the Rectangle class."""

    # ... (rest of the test methods remain the same)

class TestRectangleStdout(unittest.TestCase):
    """Tests for __str__ and display methods of Rectangle class."""

    # ... (rest of the test methods remain the same)

class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for the update_args method of the Rectangle class."""

    # ... (rest of the test methods remain the same)

class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for the update_kwargs method of the Rectangle class."""

    # ... (rest of the test methods remain the same)

if __name__ == "__main__":
    unittest.main()

