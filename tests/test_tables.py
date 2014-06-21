import unittest
import simplerestler
from simplerestler.element import TitleElement

class TablesTestCase(unittest.TestCase):
    """Tests for Tables for `element.py`."""

    def test_tables(self):
        """Table Tests"""
        d = simplerestler.Document()

        result = """
==== ========= 
Name City      
==== ========= 
John London    
---- --------- 
Jane Liverpool 
==== ========= 

"""

        table = d.table([
            ["Name", "City"],
            ["John", "London"],
            ["Jane", "Liverpool"]
            ])

        self.assertEqual(str(table), result)

        result = """
==== ==== 
Name City 
==== ==== 

"""

        table = d.table([
            ["Name", "City"]
            ])

        self.assertEqual(str(table), result)


    def test_tables_empty(self):
        """Table Tests Empty"""
        d = simplerestler.Document()

        self.assertEqual(str(d.table()), "")

        self.assertEqual(str(d.table([])), "")

if __name__ == '__main__':
    unittest.main()