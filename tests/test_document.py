import unittest
import simplerestler

class DocumentTestCase(unittest.TestCase):
    """Tests for `document.py`."""

    def test_document_elements_instances(self):
        """Document Tests"""
        d = simplerestler.Document()

        self.assertEqual(str(d), '')

        ul = d.ul("One", "Two", "Three")

        self.assertIsInstance(ul, simplerestler.element.Element)

        self.assertEqual("UlElement", d.getClassName("ul"))
        self.assertEqual("TitleElement", d.getClassName("title"))
        self.assertEqual("Element", d.getClassName(""))
        
    def test_document_error(self):
        """Document Error"""
        d = simplerestler.Document()

        with self.assertRaises(simplerestler.errors.InvalidMethodError):
            d.video()
        
if __name__ == '__main__':
    unittest.main()