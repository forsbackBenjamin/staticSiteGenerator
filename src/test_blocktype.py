import unittest

from blocktype import BlockType, block_to_block_type, markdown_to_blocks
class TestTextNode(unittest.TestCase):
    def test_quote(self):
        block = ">testing \n>testing \n>testing \n>testing"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
    def test_heading1(self):
        block = "#testing testing testing testing"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING) 
    def test_heading2(self):
        block = "######testing testing testing testing"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
    def test_not_heading1(self):
        block = "#######testing testing testing testing"
        self.assertNotEqual(block_to_block_type(block), BlockType.HEADING)
    def test_code(self):
        block = "```testing testing testing \n>testing```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
    def test_not_code(self):
        block = "```testing testing testing \n>testing``"
        self.assertNotEqual(block_to_block_type(block), BlockType.CODE)
    def test_quote(self):
        block = "-testing \n-testing \n-testing \n-testing"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
    def test_quote(self):
        block = ".testing \n.testing \n.esting \n.testing"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
    def test_markdown_to_blocks(self):
        md = "This is **bolded** paragraph   \n\n\n       This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line\n\n\n\n\n- This is a list\n- with items\n"     
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )


if __name__ == "__main__":
    unittest.main()