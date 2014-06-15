import unittest
import simplerestler

class DocumentTestCase(unittest.TestCase):
    """Tests for `document.py`."""

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

        self.assertEqual(str(d), result)
    
        d = simplerestler.Document()
        ul = d.ol("One", "Two", "Three")

        result = """
1. One
2. Two
3. Three

"""

        self.assertEqual(str(d), result)

if __name__ == '__main__':
    unittest.main()