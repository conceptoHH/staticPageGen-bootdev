import unittest
from textnode import *
from htmlnode import *


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

    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
    
    def test_bold(self):
        node = TextNode("This is a bold text node", TextType.BOLD_TEXT)
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value,"This is a bold text node")
        self.assertEqual(html_node.to_html(),"<b>This is a bold text node</b>")
    
    def test_img(self):
        node = TextNode("This is a image text node", TextType.IMAGE, "/img/1")
        html_node = text_node_to_html(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props,{"src": node.url, "alt": node.text})
        self.assertEqual(html_node.to_html(),'<img src="/img/1" alt="This is a image text node"></img>')

if __name__ == "__main__":
    unittest.main()
