import unittest
import simplerestler

class LineblocksTestCase(unittest.TestCase):
    """Tests for `elements.py`."""

    def test_lb(self):
        """Lists Tests"""
        d = simplerestler.Document()
        lb = d.lineblock("These lines are", "broken exactly like in", "the source file.")

        result = """
| These lines are
| broken exactly like in
| the source file.
"""

        self.assertEqual(str(lb), result)


if __name__ == '__main__':
    unittest.main()