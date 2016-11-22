class Node:
    """Represents a Node in the Graph."""
    def __init__(self, url):
        self._children_set = set()
        self._url = url

    def add_child(self, node):
        self._children_set.add(node)

