class Node:
    """Represents a Node in the Graph."""
    def __init__(self, url):
        self._pointed_nodes_set = set()
        self._pointed_by_nodes_set = set()
        self._url = url

    def add_pointed_node(self, node):
        self._pointed_nodes_set.add(node)
        node._pointed_by_nodes_set.add(self)
