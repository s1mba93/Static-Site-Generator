from textnode import TextNode, TextType


def main():
    text_node = TextNode("This is a test", TextType.LINK, "https://www.boot.dev")
    
    print(text_node)


main()