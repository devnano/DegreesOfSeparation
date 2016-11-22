class Node:
    """Represents a Node in the Graph."""
    def __init__(self, url):
        self._children_set = set()
        self._url = url

    def add_child(self, node):
        self._children_set.add(node)

# generation code

generated_link_base_name = "generated_link_base_name_%d"

def generate_link_name(index):
    return generated_link_base_name % index

def generate_unique_links(n):
    links = {generate_link_name(x + 1) for x in range(1, n)}
    return links
