import unittest
import simplerestler

class DocumentTestCase(unittest.TestCase):
    """Tests for `document.py`."""

    def test_doc(self):
        """Document Tests"""
        d = simplerestler.Document()
        ul = d.ul("One", "Two", "Three")
        ol = d.ol("Uno", "Dos", "Tres")

        self.assertIsInstance(ol, simplerestler.element.Element)
        self.assertIsInstance(ul, simplerestler.element.Element)

        
if __name__ == '__main__':
    unittest.main()