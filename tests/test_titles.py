import unittest
import simplerestler
from simplerestler.element import TitleElement

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

        self.assertEqual(str(d), result)

#     def test_title2(self):
#         """Title Tests 2"""
#         d = simplerestler.Document()
#         d.title(text="Chapter One", type="=")

#         result = """
# Chapter One
# ===========
# """

#         self.assertEqual(str(d), result)
    
#     def test_title_direct_params(self):
#         """Title Tests Defaults"""

#         e = TitleElement()("Chapter One", "=")
#         result = """
# Chapter One
# ===========
# """
#         x = getattr(simplerestler.element, "TitleElement")
#         print x("Ch", "^")
        
#         # self.assertEqual(str(e), result)

if __name__ == '__main__':
    unittest.main()