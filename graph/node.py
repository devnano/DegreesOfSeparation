from collections import OrderedDict

class Node:
    """Represents a Node in the Graph."""

    _all_nodes = dict()

    def __init__(self, name):
        self._children_map = OrderedDict()
        self._name = name
        self._are_all_children_created = False

    def add_child(self, node):
        self._children_map[node._name] = node
        
    def are_all_children_created(self):
        return self._are_all_children_created

    def set_all_children_created(self):
        self._are_all_children_created = True

    def children(self):
        return self._children_map.values()

    def depth(self):
        return self._depth(set())

    def hierarchical_str(self):
        str_segments = list()
        self._hierarchical_str(str_segments)

        return "\n".join(str_segments)

    def _hierarchical_str(self, str_segments, level=0, i_sibling=0, n_siblings=1, indent_str=''):
        segment = "%s%s%s" % (indent_str, hierarchical_str_prefix(level, i_sibling, n_siblings), self._name)
        str_segments.append(segment)

        indent_str = "%s%s" % (indent_str, get_hierarchical_indent(level, i_sibling, n_siblings))

        i = 0
        n = len(self.children())
        for child in self.children():
            child._hierarchical_str(str_segments, level + 1, i, n, indent_str)
            i = i + 1
    
    def _depth(self, branch):
#        branch_len = lambda b: len(b)
        if self in branch:
            # We hit a loop, return branch len:
            return len(branch)

        branch.add(self)

        if len(self.children()) == 0:
            # We are a leaf, return len
            return len(branch)

        max_depth = 0
        for child in self.children():
            # create a new branch
            child_depth = child._depth(branch.copy())
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

    def __str__(self):
        return self._name

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
        return "└──"

    return "├──"

def get_hierarchical_indent(parent_level, i_sibling, n_siblings):
    assert i_sibling < n_siblings

    if(parent_level == 0):
        return ""

    return "   " if i_sibling == n_siblings -1 else "|  "

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
        child_node = Node.create(child_name)        
        node.add_child(child_node)

    node.set_all_children_created()

def generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children):
    if(levels == 1 or root_node.are_all_children_created()):
        # Recursion ending condition
        return
    n = randrange(min_children, max_children)
    generate_node_random_names(root_node, unique_node_names, n)
    for child in root_node.children():
        generate_n_node_levels(child, unique_node_names, levels - 1, min_children, max_children)



