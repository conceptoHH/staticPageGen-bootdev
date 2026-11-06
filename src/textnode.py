from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    PLAIN_TEXT = "plain"
    BOLD_TEXT = "bold"
    ITALIC_TEXT = "italic"
    CODE_TEXT = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self,text: str, text_type: TextType, url=None) -> None:
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self,other) -> bool:
        are_equal = True
        if self.text != other.text:
            are_equal = False
        if self.text_type != other.text_type:
            are_equal = False
        if self.url != other.url:
            are_equal = False
        return are_equal
    
    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html(text_node: TextNode) -> LeafNode:
    
    match text_node.text_type:
        case TextType.PLAIN_TEXT:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD_TEXT:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC_TEXT:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE_TEXT:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": f"{text_node.url}"})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": f"{text_node.url}", "alt": f"{text_node.text}"})



