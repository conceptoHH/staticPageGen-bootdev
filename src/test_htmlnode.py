import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq_html_node(self):
        htmlnode = HTMLNode("a","a",[],{})
        htmlnode2 = HTMLNode("a","a",[],{})
        self.assertIsNotNone(htmlnode)

    def test_not_eq(self):
        node1 = HTMLNode("tag1", "val1")
        node2 = HTMLNode("tag2", "val2")
        self.assertNotEqual(node1,node2)

    def test_props(self):
        node1 = HTMLNode("test","sd",[],{"prop1":"val"})
        self.assertIsInstance(node1.props_to_html(),str)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
if __name__ == "__main__":
    unittest.main()
