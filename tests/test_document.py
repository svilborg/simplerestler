import unittest
import simplerestler

class DocumentTestCase(unittest.TestCase):
    """Tests for `document.py`."""

    def test_document_elements_instances(self):
        """Document Tests"""
        d = simplerestler.Document()
        ul = d.ul("One", "Two", "Three")
        ol = d.ol("Uno", "Dos", "Tres")

        self.assertIsInstance(ol, simplerestler.element.Element)
        self.assertIsInstance(ul, simplerestler.element.Element)
    

    def test_document_elements_image(self):
        """Image Tests"""
        d = simplerestler.Document()
        image = d.image(src="http://google.com/image.png")

        self.assertIsInstance(image, simplerestler.element.Element)


    def test_document_elements(self):
        """Lists Tests"""
        d = simplerestler.Document()
        ul = d.ul("One", "Two", "Three")

        result = """
* One
* Two
* Three

"""

        self.assertEqual(d.__str__(), result)
    
        d = simplerestler.Document()
        ul = d.ol("One", "Two", "Three")

        result = """
1. One
2. Two
3. Three

"""

        self.assertEqual(d.__str__(), result)

if __name__ == '__main__':
    unittest.main()