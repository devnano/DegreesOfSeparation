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

    def depth(self):
        return self._depth(0)

    def _depth(self, current_level):
        if len(self.children()) == 0:
            # We are a leaf
            return current_level

        max_depth = 0
        for child in self.children():
            child_depth = child._depth(current_level + 1)
            max_depth = child_depth if child_depth > max_depth else max_depth

        return max_depth

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

def generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children):
    if(levels == 0):
        # Recursion ending condition
        return
    n = randrange(min_children, max_children)
    generate_node_random_names(root_node, unique_node_names, n)
    for child in root_node.children():
        generate_n_node_levels(child, unique_node_names, levels - 1, min_children, max_children)
