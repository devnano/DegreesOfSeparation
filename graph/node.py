class Node:
    _all_nodes = set()
    """Represents a Node in the Graph."""
    def __init__(self, url):
        self._children_set = set()
        self._url = url
        self.__class__._all_nodes.add(self)

    def add_child(self, node):
        self._children_set.add(node)

    @classmethod
    def get_all_nodes(self):
        return self._all_nodes

# generation code

from random import randrange

generated_link_base_name = "generated_link_base_name_%d"

def generate_link_name(index):
    return generated_link_base_name % index

def generate_unique_links(n):
    links = {generate_link_name(x + 1) for x in range(0, n)}
    return links

def generate_random_links(source_links, n):
    assert len(source_links) > n
    child_links = set()
    l = list(source_links)

    while not len(child_links) == n:
        link = l[randrange(0, len(source_links))]
        child_links.add(link)
    
    return child_links

def generate_node_random_links(node, source_links, n):
    child_links = generate_random_links(source_links, n)

    for child_link in child_links:
        child_node = Node(child_link)
        node.add_child(child_node)
