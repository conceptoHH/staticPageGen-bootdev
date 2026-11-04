class HTMLNode():
    def __init__(self, 
                 tag: str | None = None, 
                 value: str | None = None, 
                 children: list[HTMLNode] | None = None, 
                 props: dict[str,str] | None = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Method to_html not implemented yet")

    def props_to_html(self):
        if self.props is None:
            return ""
        props_str = ""
        for k in self.props:
            props_str += f' {k}="{self.props[k]}"'
        return props_str
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self,tag: str | None,value: str | None,props: dict[str,str] | None = None ):
        super().__init__(tag,value,None,props)

    def to_html(self):
        if self.props is None:
            return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return f'<{self.tag}{self.props_to_html}>{self.value}</{self.tag}>'
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list[HTMLNode], props: dict[str,str] | None = None):
        super().__init__(tag,None,children,props)

    
