import unittest
import get_tissue_samples
import os
import sys

class TestTissueSamples(unittest.TestCase):
    
    def test_linear_search(self):
        L = [0, 1, 2, 3]
        # First test whether we return the first key location
        r = get_tissue_samples.linear_search(0, L)
        self.assertEqual(r, 0)
        # then test whether we return a last value
        r = get_tissue_samples.linear_search(3, L)
        self.assertEqual(r, 3)
        # Then whether we get a -1 if the value isn't present
        r = get_tissue_samples.linear_search(5, L)
        self.assertEqual(r, -1)

    def test_fetch_metadata(self):
        group = 'SMTS'
        meta_file = 'GTEx_Analysis_v8_Annotations_SampleAttributesDS.txt'
        r = get_tissue_samples.fetch_metadata(group, meta_file)
        # Check that first entry contains blood
        self.assertIn('Blood', r[0])
        # Check that second entry is the keys
        self.assertIn('Salivary Gland', r[1])

if __name__ == '__main__':
    unittest.main()
