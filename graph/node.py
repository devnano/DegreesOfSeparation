class Node:
    """Represents a Node in the Graph."""

    _all_nodes = dict()

    def __init__(self, name):
        self._children_set = set()
        self._name = name

    def add_child(self, node):
        self._children_set.add(node)

    def children(self):
        return self._children_set

    def __hash__(self):
        return hash(self._name)

    def __eq__(self, other):
        """Override the default Equals behavior"""
        if isinstance(other, self.__class__):
            return self._name == other._name
        return False

    def __ne__(self, other):
        """Define a non-equality test"""
        return not self.__eq__(other)

    @classmethod
    def create(cls, name):
        if name in cls._all_nodes:
            return cls._all_nodes[name]

        node = Node(name)
        cls._all_nodes[name] = node
        return node

    @classmethod
    def get_all_nodes(cls):
        return cls._all_nodes

# generation code

from random import randrange

generated_name_base_name = "generated_name_base_name_%d"

def generate_name_name(index):
    return generated_name_base_name % index

def generate_unique_names(n):
    names = {generate_name_name(x + 1) for x in range(0, n)}
    return names

def generate_random_names(source_names, n):
    assert len(source_names) > n
    child_names = set()
    l = list(source_names)

    while not len(child_names) == n:
        name = l[randrange(0, len(source_names))]
        child_names.add(name)
    
    return child_names

def generate_node_random_names(node, source_names, n):
    child_names = generate_random_names(source_names, n)

    for child_name in child_names:
        child_node = Node(child_name)
        node.add_child(child_node)
