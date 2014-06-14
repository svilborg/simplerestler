import unittest
import simplerestler

class TitlesTestCase(unittest.TestCase):
    """Tests for Titles for `element.py`."""

    def test_title(self):
        """Title Tests"""
        d = simplerestler.Document()
        title = d.title(text="Chapter One", type="*")

        print title

        self.assertIsInstance(title, simplerestler.element.Element)

    def test_title2(self):
        """Title Tests 2"""
        d = simplerestler.Document()
        title = d.title(text="Chapter One", type="=")

        print title

        self.assertIsInstance(title, simplerestler.element.Element)

if __name__ == '__main__':
    unittest.main()