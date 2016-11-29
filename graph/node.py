from collections import OrderedDict
import pdb

class Node:
    """Represents a Node in the Graph."""

    _all_nodes = dict()

    def __init__(self, name):
        self._children_dict = OrderedDict()
        self._name = name
        self._are_all_children_created = False

    def name(self):
        return self._name

    def add_child(self, node):
        self._children_dict[node._name] = node
        
    def are_all_children_created(self):
        return self._are_all_children_created

    def set_all_children_created(self):
        self._are_all_children_created = True

    def children(self):
        return self._children_dict.values()

    def get_node(self, index_path):
        n = len(index_path)
        if(n == 0):
            return None

        child_node = list(self.children())[index_path[0]]

        if(n == 1):
            return child_node

        return child_node.get_node(index_path[1:])

    def max_depth(self):                
#        pdb.set_trace()
        return self._max_depth(set())

    def _max_depth(self, branch):
        if self in branch:
            # We hit a loop, max_depth
            return len(branch)

        branch.add(self)

        if len(self.children()) == 0:
            # We are a leaf, return len
            return len(branch)

        max_depth = 0
        for child in self.children():
            # create a new branch
            child_max_depth = child._max_depth(branch.copy())
            max_depth = child_max_depth if child_max_depth > max_depth else max_depth

        return max_depth

    def hierarchical_str(self):
        str_segments = list()
        self._hierarchical_str(str_segments, list())

        return "\n".join(str_segments)

    def _hierarchical_str(self, str_segments, branch, level=0, i_sibling=0, n_siblings=1, indent_str=''):
        segment = "%s%s%s" % (indent_str, hierarchical_str_prefix(level, i_sibling, n_siblings), self._name)
        str_segments.append(segment)

        if self in branch:
            # We hit a loop, max_depth
            return ""

        branch.append(self)

        indent_str = "%s%s" % (indent_str, get_hierarchical_indent(level, i_sibling, n_siblings))

        i = 0
        n = len(self.children())
        for child in self.children():
            child._hierarchical_str(str_segments, branch.copy(), level + 1, i, n, indent_str)
            i = i + 1
    
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

    def __str__(self):
        return self._name

# In Memory Fetch

    def in_memory_fetch(self, source_root_node):
        source_root_node
        self._children_dict = {name:Node(name) for name in source_root_node._children_dict}

# Class methods

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


# util function

def hierarchical_str_prefix(level, i_sibling, n_siblings):
    assert i_sibling < n_siblings

    if level == 0:
        return ""

    if n_siblings == 1 or i_sibling == n_siblings -1:
        return "└── "

    return "├── "

def get_hierarchical_indent(parent_level, i_sibling, n_siblings):
    assert i_sibling < n_siblings

    if(parent_level == 0):
        return ""

    return "    " if i_sibling == n_siblings -1 else "|   "

# generation code

# random

from random import randrange

all_random_ints_generated = list()

def _randrange(start, stop):
    i = randrange(start, stop)
    all_random_ints_generated.append(i)
    return i

def reset_all_random_ints_generated():
    all_random_ints_generated = list()

generated_name_base_name = "generated_name_base_name_%d"

def generate_name_name(index):
    return generated_name_base_name % index

def generate_unique_names(n):
    names = {generate_name_name(x + 1) for x in range(0, n)}
    return names

def generate_random_names(source_names, n, randr=_randrange):
    assert len(source_names) > n
    child_names = list()
    l = list(source_names)

    while not len(child_names) == n:
        name = l[randr(0, len(source_names))]
        if name in child_names:
            continue

        child_names.append(name)
    
    return child_names

def generate_node_random_names(node, source_names, n, randr=_randrange):
    child_names = generate_random_names(source_names, n, randr)

    for child_name in child_names:
        child_node = Node.create(child_name)        
        node.add_child(child_node)

    node.set_all_children_created()

def generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children, randr=_randrange):
    if(levels == 1 or root_node.are_all_children_created()):
        # Recursion ending condition
        return
    n = randr(min_children, max_children)

    generate_node_random_names(root_node, unique_node_names, n, randr)
    for child in root_node.children():
        generate_n_node_levels(child, unique_node_names, levels - 1, min_children, max_children, randr)

# Main Executable

import sys

if __name__ == "__main__":
    print(sys.argv[1:])
    get_int_arg = lambda i, d: int(sys.argv[i]) if len(sys.argv) > i else d
    n_nodes = get_int_arg(1, 100)
    levels = get_int_arg(2, 5)
    min_children_per_level = get_int_arg(3, 1)
    max_children_per_level = get_int_arg(4, 10)

    unique_names = list(generate_unique_names(n_nodes))
    root_node = Node.create(unique_names[0])

    reset_all_random_ints_generated()
    generate_n_node_levels(root_node, unique_names, levels, min_children_per_level, max_children_per_level)
    print(root_node.hierarchical_str())
    print(all_random_ints_generated)
