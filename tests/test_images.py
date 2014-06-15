import unittest
import simplerestler

class ImageTestCase(unittest.TestCase):
    """Tests for `element.py`."""

    def test_document_elements_image(self):
        """Image Tests"""
        d = simplerestler.Document()
        image = d.image(src="http://images/1.png")
        
        result = """
.. image:: http://images/1.png
"""

        self.assertEqual(str(image), result)

        image2 = d.image(src="http://images/1.png", height="100px", width="100px", alt="alt text")

        result = """
.. image:: http://images/1.png
   :alt: alt text
   :height: 100px
   :width: 100px
"""
        self.assertEqual(str(image2), result)

    def test_document_error(self):
        """Image Tests"""
        
        d = simplerestler.Document()
        self.assertRaises(simplerestler.errors.InvalidElementError, d.image)

if __name__ == '__main__':
    unittest.main()