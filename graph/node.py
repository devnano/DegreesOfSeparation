class Node:
    """Represents a Node in the Graph."""
    def __init__(self, url):
        self.pointed_nodes_set = set()
        self.pointed_by_nodes_set = set()
        self.url = url

    def add_pointed_node(self, node):
        self.pointed_nodes_set.add(node)
        node.pointed_by_nodes_set.add(self)
