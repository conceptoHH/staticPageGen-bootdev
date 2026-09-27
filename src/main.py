from textnode import *

def main():
    tnList = [ 
    TextNode("plaintext",TextType.PLAIN_TEXT),
    TextNode("texto2",TextType.BOLD_TEXT),
    TextNode("texto3",TextType.ITALIC_TEXT),
    TextNode("texto4",TextType.LINK,"https://example.com")
    ]
    for n in tnList:
        print(n)

if __name__ == "__main__":
    main()
