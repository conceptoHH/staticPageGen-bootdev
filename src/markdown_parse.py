from textnode import *

def split_nodes_delimiter(old_nodes: list[TextNode], delimiter: str, text_type: TextType) -> list[TextNode]:
    new_nodes = []
    for oldn in old_nodes:
        
        tmp_str=""
        cont=0
        split_result = []

        if oldn.text_type != TextType.PLAIN_TEXT:
            new_nodes.append(oldn)

        for c in oldn:
            
            if c == delimiter:
                cont++

            if cont >= 1 and cont <= 2:
                tmp_str += c

        if cont == 1:
            raise Exception("Invalid markdown text")

        if cont == 2:
            split_result = oldn.split(delimiter)
            
            for s in split_result:
                if s == tmp_str:
                    new_nodes.append(TextNode(s,text_type))
                else:
                    new_nodes.append(TextNode(s,TextType.PLAIN_TEXT))
    return new_nodes
