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

    def fetch(self, fetch_strategy):
        fetch_strategy(self)
        self.set_all_children_created()

    def search(self, node, fetch_strategy):
        return self._search(node, fetch_strategy, [], set())

    def _search(self, node, fetch_strategy, index_path, branch):
        pass

    def _search_at_level(self, node, level, fetch_strategy=None, index_path=None, branch=None):
        assert level >= 1

        if branch and self in branch:
            # We hit a loop, not found
            return []
        
        if not index_path:
            index_path = []

        if not branch:
            branch = set()

        branch.add(self)

        if not self.are_all_children_created():
            self.fetch(fetch_strategy)
            
        children = list(self.children())

        for i in range(0, len(children)):
            child_index_path = index_path.copy()
            child_index_path.append(i)
            child = children[i]

            if level == 1:
                found_index_path = child_index_path if child == node else []
            else:
                found_index_path = child._search_at_level(node, level - 1, fetch_strategy, child_index_path, branch.copy())

            if found_index_path != []:
                return found_index_path

        return []

    def hierarchical_str(self):
        str_segments = list()
        self._hierarchical_str(str_segments, list())

        return "".join(str_segments)

    def _hierarchical_str(self, str_segments, branch, level=0, i_sibling=0, n_siblings=1, indent_str=''):
        segment = "%s%s%s\n" % (indent_str, hierarchical_str_prefix(level, i_sibling, n_siblings), self._name)
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


    # Parse tree:
    @classmethod
    def parse_tree(cls, tree_str):
        tree_str = tree_str.strip(" \t\n\r")
        lines = tree_str.split("\n")

        return cls._parse_lines(lines)

    @classmethod
    def _parse_lines(cls, lines, root_node=None, current_level=0):
        if lines == []: return None
        if (not root_node and current_level != 0) or (root_node and current_level == 0): raise Node.SyntaxError("")

        previous_node = None

        while len(lines):
            result = cls._parse_line(lines[0])
            level = result[0]
            node = result[1]
            node.set_all_children_created()

            if level == current_level:
                if root_node:
                    root_node.add_child(node)
                # Consume current line
                del lines[0]
            elif level == current_level + 1: 
                cls._parse_lines(lines, previous_node, current_level + 1)
                continue
            elif level < current_level: 
                return
            else: 
                raise Node.SyntaxError("")

            previous_node = node

        return previous_node if not root_node else None

    @classmethod
    def _parse_line(cls, line):
        level = 0
        last_child_prefix = "└── "
        final_level_prefixes = {"├── "}
        middle_level_prefixes = {"    ", "|   "}
        final_level_prefixes.add(last_child_prefix)
        is_last_child = True
        
        while(True):
            level_prefix = line[0:4]
            
            if not level_prefix in final_level_prefixes | middle_level_prefixes:
                break

            level += 1
            line = line[4:]

            if level_prefix in final_level_prefixes:
                is_last_child = level_prefix == last_child_prefix
                break

        return (level, Node.create(line), is_last_child)

    class SyntaxError(Exception):
        def __init__(self,*args,**kwargs):
            Exception.__init__(self,*args,**kwargs)


# util functions

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

    print(unique_names)
    print(root_node.hierarchical_str())
    print(all_random_ints_generated)
