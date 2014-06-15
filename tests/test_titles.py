import unittest
import simplerestler

class TitlesTestCase(unittest.TestCase):
    """Tests for Titles for `element.py`."""

    def test_title(self):
        """Title Tests"""
        d = simplerestler.Document()
        title = d.title(text="Chapter One", type="*")

        self.assertIsInstance(title, simplerestler.element.Element)
        result = """
Chapter One
***********
"""

        self.assertEqual(d.__str__(), result)

    def test_title2(self):
        """Title Tests 2"""
        d = simplerestler.Document()
        title = d.title(text="Chapter One", type="=")

        self.assertIsInstance(title, simplerestler.element.Element)

if __name__ == '__main__':
    unittest.main()