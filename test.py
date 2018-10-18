#!/usr/bin/python
from utility.Utility import *
from utility.DnaData import *
import unittest

class TestDNAConverter(unittest.TestCase):

    def test_with_expected_results(self):
        dnaParser = DnaData("dna_conversion_samples/input")

        myOutput7 = dnaParser.print_FASTQ(7,False)
        myOutput15 = dnaParser.print_FASTQ(15,False)
        myOutput80 = dnaParser.print_FASTQ(80,False)

        refOutput7 = Utility.read_file("dna_conversion_samples/output7")
        refOutput15 = Utility.read_file("dna_conversion_samples/output15")
        refOutput80 = Utility.read_file("dna_conversion_samples/output80")

        self.assertEqual(myOutput7, refOutput7)
        self.assertEqual(myOutput15, refOutput15)
        self.assertEqual(myOutput80, refOutput80)

if __name__ == '__main__':
    unittest.main()