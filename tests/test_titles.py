import unittest
import simplerestler
from simplerestler.element import TitleElement

class TitlesTestCase(unittest.TestCase):
    """Tests for Titles for `element.py`."""

    def test_title(self):
        """Title Tests"""
        e = TitleElement()(text="Chapter One", type="*")

        result = """
Chapter One
***********
"""

        self.assertEqual(str(e), result)

        e = TitleElement()(text="Chapter One", type="=")

        result = """
Chapter One
===========
"""

        self.assertEqual(str(e), result)
    
    def test_title_direct_params(self):
        """Title Tests Defaults"""

        e = TitleElement()("Chapter One", "=")
        result = """
Chapter One
===========
"""
        
        self.assertEqual(str(e), result)

if __name__ == '__main__':
    unittest.main()