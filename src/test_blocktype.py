import unittest

from blocktype import BlockType, block_to_block_type, markdown_to_blocks
class TestTextNode(unittest.TestCase):
    def test_quote(self):
        block = ">testing \n>testing \n>testing \n>testing"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_heading1(self):
        block = "#testing testing testing testing"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_not_heading1(self):
        block = "#######testing testing testing testing"
        self.assertNotEqual(block_to_block_type(block), BlockType.HEADING)
if __name__ == "__main__":
    unittest.main()