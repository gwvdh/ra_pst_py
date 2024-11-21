from src.core import * 
from src.file_parser import *

import unittest
from lxml import etree

class CoreTest(unittest.TestCase):
    
    def test_allocation(self):
        target = etree.parse("tests/test_comparison_data/allocation.xml")
        process = parse_process_file("tests/test_data/test_process.xml")
        resources = parse_resource_file("tests/test_data/test_resource.xml")
        ra_pst = RA_PST(process, resources)
        ra_pst.get_ra_pst()
        ra_pst.save_ra_pst("tests/outcome/ra_pst.xml")
        created = etree.parse("tests/test_comparison_data/allocation.xml")

        self.assertEqual(etree.tostring(created), etree.tostring(target))
