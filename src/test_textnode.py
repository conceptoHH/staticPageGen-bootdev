import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD_TEXT)
        node2 = TextNode("This is a text node", TextType.BOLD_TEXT)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("test not eq", TextType.CODE_TEXT)
        node2 = TextNode("test not eq", TextType.ITALIC_TEXT)
        self.assertNotEqual(node1,node2)

    def test_image(self):
        node1 = TextNode("test image", TextType.IMAGE,"/img/1")
        node2 = TextNode("test image", TextType.IMAGE,"/img/2")
        self.assertIsInstance(node1,TextNode)
        self.assertIsInstance(node2,TextNode)

    def test_urlIsNone(self):
        node1 = TextNode("test url none", TextType.PLAIN_TEXT)
        self.assertIsNone(node1.url)

    def test_urlIsNotNone(self):
        node1 = TextNode("test url none", TextType.LINK,"https://example.foo")
        self.assertIsNotNone(node1.url)
if __name__ == "__main__":
    unittest.main()
