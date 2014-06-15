import unittest
from simplerestler.utils import Utils

class UtilsTestCase(unittest.TestCase):
    """Tests for `utils.py`."""

    def test_title(self):
        """Title Tests"""
        # test = Utils.html_escape("Some <b>test</b> <B>test</B>")
        # print test

        self.assertEqual("Live on radio", Utils.ireplace("tv", "radio", "Live on tv"))
        self.assertEqual("Live on radio", Utils.ireplace("tv", "radio", "Live on TV"))
        self.assertEqual("Live on radio", Utils.ireplace("tv", "radio", "Live on Tv"))
        self.assertEqual("Live on radio", Utils.ireplace("tv", "radio", "Live on tV"))
        self.assertEqual("Live on radio", Utils.ireplace("TV", "radio", "Live on tV"))
        self.assertEqual("Live on radio", Utils.ireplace("tv", "radio", "Live on tV"))

        self.assertEqual("**Live** on **TV**", Utils.html_rest("<b>Live</b> on <B>TV</B>"))
        self.assertEqual("*Live* on **TV**", Utils.html_rest("<em>Live</em> on <B>TV</B>"))
        
if __name__ == '__main__':
    unittest.main()