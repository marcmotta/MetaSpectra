# test_metaspectra.py
"""
Tests for MetaSpectra module.
"""

import unittest
from metaspectra import MetaSpectra

class TestMetaSpectra(unittest.TestCase):
    """Test cases for MetaSpectra class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaSpectra()
        self.assertIsInstance(instance, MetaSpectra)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaSpectra()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
