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

        self.assertEqual(str(comment), result)        

    def test_document_p(self):
        """Paragraph Tests"""
        d = simplerestler.Document()
        p = d.p("This paragraph is on the first line This is the same line")

        result = """
This paragraph is on the first line This is the same line
"""

        self.assertEqual(str(p), result)

        p = d.p("This paragraph is on the first line\nThis is a new line")

        result = """
This paragraph is on the first line
 This is a new line
"""

        self.assertEqual(str(p), result) 

        p = d.p("This <b>paragraph</b> is on the first line<br/>This is a new line")

        result = """
This **paragraph** is on the first line
 This is a new line
"""

        self.assertEqual(str(p), result)        


    def test_document_p(self):
        """Pre Tests"""
        d = simplerestler.Document()
        pre = d.pre("Literal - * and ** and ``")

        result = """
::

 Literal - * and ** and ``
"""

        self.assertEqual(str(pre), result)


if __name__ == '__main__':
    unittest.main()