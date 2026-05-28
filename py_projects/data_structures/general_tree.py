class Tree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent  = None

    def add_child(self, child):
        child.parent = self #child will also become parent at some point if that child also has its own children
        self.children.append(child)

    def print_tree(self, level=0):
        # Create indentation based on the current depth level
        spaces = "   " * level
        # If it's a child node, add a little branch prefix for visuals
        prefix = spaces + "|__ " if level > 0 else ""

        print(prefix + self.data)

        # Recursively print all children, increasing the level
        for child in self.children:
            child.print_tree(level + 1)

def build_tree():
    root  = Tree("Electronics")

    # first child of electronics parent
    laptop =  Tree("Laptop")
    laptop.add_child(Tree("HP"))
    laptop.add_child(Tree("Macbook"))

    #second child of electronics parent
    phone = Tree("Phone")
    phone.add_child(Tree("iPhone"))
    phone.add_child(Tree("Samsung"))

    #third child of electronics parent
    speaker = Tree("Speaker")
    speaker.add_child(Tree("Bose"))
    speaker.add_child(Tree("JBL"))

    # add children to the root
    root.add_child(laptop)
    root.add_child(phone)
    root.add_child(speaker)

    return root

img_tree = build_tree()
img_tree.print_tree()
