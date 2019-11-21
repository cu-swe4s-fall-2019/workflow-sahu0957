import unittest
import os
import box
import sys

class TestBox(unittest.TestCase):
    
    def test_boxplot(self):
        # Test whether it works!
        data = [[[0, 1, 2]]]
        metadata = ['foo', 'bar', 'car']
        title = ['tEST']
        box.boxplot(data, metadata, 'y_label', title, 'test.png')
        self.assertTrue(os.path.exists('test.png'))

    def test_boxplot_error(self):
        # Test error handling
        data = 'foo'
        metadata = ['foo', 'bar', 'car']
        title = ['tEST']
        with self.assertRaises(SystemExit) as err:
            box.boxplot(data, metadata, 'y_label', title, 'test.png')

if __name__ == '__main__':
    unittest.main()
