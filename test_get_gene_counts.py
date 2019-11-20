import unittest
import get_gene_counts
import os
import sys

class TestGeneCounts(unittest.TestCase):
       
    def test_fetch_gene_counts(self):
        gene = 'LDLR'
        output = 'test.txt'
        count_file = 'GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_reads.acmg_59.gct.gz'
     
        get_gene_counts.fetch_gene_counts(gene, count_file, output)
        self.assertIn(output, os.listdir('.'))

if __name__ == '__main__':
    unittest.main()
