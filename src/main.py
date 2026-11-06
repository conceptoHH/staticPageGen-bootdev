from htmlnode import *

def main():
    node = LeafNode(None,"vall")
    node2 = HTMLNode("a","vall")
    node3 = HTMLNode("f","asfda",[node,node2],{"href": "link", "target": "_blank"})
    print(node3)
    print(node3.props_to_html())
    print(node.to_html())


if __name__ == "__main__":
    main()
