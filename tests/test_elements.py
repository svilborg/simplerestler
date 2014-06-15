import unittest
import simplerestler

class ElementsTestCase(unittest.TestCase):
    """Tests for `elements.py`."""

    def test_document_lists(self):
        """Lists Tests"""
        d = simplerestler.Document()
        ul = d.ul("One", "Two", "Three")

        result = """
* One
* Two
* Three

"""

        self.assertEqual(str(d), result)
    
        d = simplerestler.Document()
        ul = d.ol("One", "Two", "Three")

        result = """
1. One
2. Two
3. Three

"""

        self.assertEqual(str(d), result)

    def test_document_comments(self):
        """Comments Tests"""
        d = simplerestler.Document()
        comment = d.comment("Comment text")

        result = """

.. Comment text

"""

#         self.assertEqual(str(comment), result)        

#         comment = d.comment("Comment text\nHere")

#         result = """

# .. Comment text

# """
#         print comment
#         print result
#         self.assertEqual(str(comment), result)

if __name__ == '__main__':
    unittest.main()