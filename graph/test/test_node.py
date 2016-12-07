from node import Node
from node import *
import pdb

import pytest

# tests setup

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    Node._all_nodes = dict()
    create_deterministic_randrange([8, 17, 7, 2, 44, 48, 14, 34, 13, 8, 41, 5, 42, 22, 21, 11, 12, 29, 1, 3, 2, 2, 11, 3, 16, 14, 8, 1, 44, 6, 39, 39, 19, 12, 46, 47, 42, 3, 39, 1, 45, 5, 20, 27, 44, 30, 47])

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """
# testing random stuff
from random import randrange

deterministic_randrange = None

def create_deterministic_randrange(rand_ints):
    def randrange_generator(rand_ints=rand_ints):
        for r in rand_ints:
            yield r

    generator = randrange_generator()

    def _deterministic_randrange(start, end, generator=generator):
        r = next(generator)

        try:
            _deterministic_randrange.all_rand_ints.append(r)
        except:
            _deterministic_randrange.all_rand_ints = list()
            _deterministic_randrange.all_rand_ints.append(r)

        return r

    global deterministic_randrange
    deterministic_randrange = _deterministic_randrange

def test_deterministic_randrange_generation():
    i = deterministic_randrange(1, 10)
    assert i == 8
    i = deterministic_randrange(1, 10)
    assert i == 17

def test_deterministic_randrange_generation_second_run():
    i = deterministic_randrange(1, 10)
    assert i == 8
    i = deterministic_randrange(1, 10)
    assert i == 17

# core functionlality tests

def test_name_correct_after_creation():
    name = "name"
    n = Node(name)
    assert n._name == name

def test_name_method_correct_after_creation():
    name = "name"
    n = Node(name)
    assert n.name() == name
    

def test_children_set_after_creation():
    n = Node("")
    assert n._children_dict is not None

def test_is_child_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_child(n2)
    assert n2 in n1.children()

def test_children_len_before_any_add():
    n1 = Node("")

    assert len(n1.children()) == 0

def test_children_len_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_child(n2)
    assert len(n1.children()) == 1

def test_not_all_children_created():
    n = Node("")
    assert not n.are_all_children_created()

def test_all_children_created():
    n = Node("")
    n.set_all_children_created()
    assert n.are_all_children_created()

def test_node_all_nodes_len():
    root_node = Node("")
    all_nodes = Node.get_all_nodes()
    assert len(all_nodes) == 0

def test_node_hash():
    name = "unique_name"
    n1 = Node(name)
    n2 = Node(name)
    assert hash(n1) == hash(n2)

def test_node_equality():
    name = "unique_name"
    n1 = Node(name)
    n2 = Node(name)
    assert n1 == n2

def test_node_inequality():
    name = "unique_name"
    n1 = Node(name)
    n2 = Node(name)
    assert (n1 != n2) is False

# class methods

def test_node_get_all_nodes_dict():
    all_nodes = Node.get_all_nodes()
    assert isinstance(all_nodes, dict)

def test_create_node_all_nodes_len_1():
    name = "test_name"
    Node.create(name)
    all_nodes = Node.get_all_nodes()
    assert len(all_nodes) == 1

def test_create_node_all_nodes_len_n(unique_node_names):
    for name in unique_node_names:
        Node.create(name)
    all_nodes = Node.get_all_nodes()
    assert len(all_nodes) == len(unique_node_names)

def test_create_node_unique_instances():
    name = "unique_name"
    n1 = Node.create(name)
    n2 = Node.create(name)
    assert n1 is n2

# generation code test
# fixture

@pytest.fixture
def unique_node_names():
    source_names = ['generated_name_base_name_20', 'generated_name_base_name_17', 'generated_name_base_name_23', 'generated_name_base_name_38', 'generated_name_base_name_16', 'generated_name_base_name_27', 'generated_name_base_name_36', 'generated_name_base_name_49', 'generated_name_base_name_11', 'generated_name_base_name_21', 'generated_name_base_name_30', 'generated_name_base_name_10', 'generated_name_base_name_26', 'generated_name_base_name_6', 'generated_name_base_name_5', 'generated_name_base_name_4', 'generated_name_base_name_35', 'generated_name_base_name_40', 'generated_name_base_name_37', 'generated_name_base_name_25', 'generated_name_base_name_13', 'generated_name_base_name_22', 'generated_name_base_name_50', 'generated_name_base_name_43', 'generated_name_base_name_9', 'generated_name_base_name_8', 'generated_name_base_name_34', 'generated_name_base_name_41', 'generated_name_base_name_46', 'generated_name_base_name_29', 'generated_name_base_name_32', 'generated_name_base_name_18', 'generated_name_base_name_42', 'generated_name_base_name_28', 'generated_name_base_name_48', 'generated_name_base_name_44', 'generated_name_base_name_12', 'generated_name_base_name_19', 'generated_name_base_name_3', 'generated_name_base_name_45', 'generated_name_base_name_39', 'generated_name_base_name_7', 'generated_name_base_name_15', 'generated_name_base_name_47', 'generated_name_base_name_2', 'generated_name_base_name_31', 'generated_name_base_name_33', 'generated_name_base_name_24', 'generated_name_base_name_14']
    return source_names

@pytest.fixture
def root_node_3_levels(unique_node_names):
    levels = 3
    min_children = 2
    max_children = 5
    root_node = Node.create(list(unique_node_names)[0])
    create_deterministic_randrange([3, 5, 9, 8, 4, 2, 2, 9, 2, 8, 7, 4, 2, 8, 0, 8, 0, 2, 1, 4, 6, 9, 6, 5, 7])
    generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children, deterministic_randrange)
    
    return root_node

# End fixtures, start generation code tests

def test_unique_node_names_order(unique_node_names):
    assert list(unique_node_names)[0] == 'generated_name_base_name_20'
    assert list(unique_node_names)[-1] == 'generated_name_base_name_14'

def test_generate_name_name():
    name_name = generate_name_name(1)
    assert "generated_name_base_name_1" == name_name

def test_generate_unique_names_len():
    n = 100
    unique_names = generate_unique_names(n)
    assert len(unique_names) == n

def test_generate_unique_names_type():
    n = 1
    unique_names = generate_unique_names(n)
    assert isinstance(unique_names, set)

def test_generate_random_names(unique_node_names):
    n = 10
    random_names = generate_random_names(unique_node_names, n)
    assert len(random_names) == n

def test_generate_random_names_error(unique_node_names):
    n = len(unique_node_names) + 1
    with pytest.raises(AssertionError):
        generate_random_names(unique_node_names, n)

def test_generate_node_random_names(unique_node_names):
    n = 10
    root_node = Node.create(unique_node_names[0])
    generate_node_random_names(root_node, unique_node_names, n)
    assert len(root_node.children()) == n

def test_max_depth_1():
    n1 = Node.create("1")

    assert n1.max_depth() == 1

def test_max_depth_loop():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)
    n2.add_child(n1)

    assert n1.max_depth() == 2

def test_max_depth_2():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)

    assert n1.max_depth() == 2

def test_max_depth_3_multi_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n21 = Node.create("21")
    n22 = Node.create("22")
    n23 = Node.create("23")

    n1.add_child(n2)
    n2.add_child(n21)
    n2.add_child(n22)
    n2.add_child(n23)

    assert n1.max_depth() == 3

def test_max_depth_3_multi_child_on_each_level():
    n1 = Node.create("1")
    n11 = Node.create("11")
    n12 = Node.create("12")
    n13 = Node.create("23")

    n111 = Node.create("111")
    n112 = Node.create("112")
    n113 = Node.create("113")

    n121 = Node.create("121")
    n122 = Node.create("122")
    n123 = Node.create("123")
    n124 = Node.create("124")

    n1.add_child(n11)
    n1.add_child(n12)
    n1.add_child(n13)

    n11.add_child(n111)
    n11.add_child(n112)
    n11.add_child(n113)

    n12.add_child(n121)
    n12.add_child(n122)
    n12.add_child(n123)
    n12.add_child(n124)

    assert n1.max_depth() == 3

def test_generate_n_node_levels(unique_node_names):
    levels = 2
    min_children = 1
    max_children = 10
    root_node = Node.create(list(unique_node_names)[0])
    generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children)
    assert len(root_node.children()) > 0 

def test_node_hierarchical_str_prefix_level_0():
    prefix = hierarchical_str_prefix(0, 0, 1)
    assert prefix == ""

def test_node_hierarchical_str_prefix_level_n_single_child():
    prefix = hierarchical_str_prefix(5, 0, 1)
    assert prefix == "└── "

def test_node_hierarchical_str_prefix_level_n_first_node_not_single_child():
    prefix = hierarchical_str_prefix(1, 0, 2)
    assert prefix == "├── "

def test_node_hierarchical_str_prefix_level_n_middle_child():
    prefix = hierarchical_str_prefix(3, 2, 5)
    assert prefix == "├── "

def test_node_hierarchical_str_prefix_level_n_last_child():
    prefix = hierarchical_str_prefix(3, 4, 5)
    assert prefix == "└── "

def test_get_hierarchical_indent_level_0_last_sibling():
    indent = get_hierarchical_indent(0, 0, 1)
    assert indent == ""

def test_get_hierarchical_indent_level_1_last_sibling():
    indent = get_hierarchical_indent(1, 0, 1)
    assert indent == "    "

def test_get_hierarchical_indent_level_1_more_sibling():
    indent = get_hierarchical_indent(1, 0, 5)
    assert indent == "|   "

def test_node_hierarchical_str_single_level():
    n1 = Node.create("1")

    assert n1.hierarchical_str() == "1\n"


def test_node_hierarchical_str_2_levels_1_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)

    assert n1.hierarchical_str() == \
"""1
└── 2
"""

def test_node_hierarchical_str_2_levels_2_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n3 = Node.create("3")
    n1.add_child(n2)
    n1.add_child(n3)

    assert n1.hierarchical_str() == \
"""1
├── 2
└── 3
"""

def test_node_hierarchical_str_3_levels_1_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n21 = Node.create("21")
    n2.add_child(n21)
    n3 = Node.create("3")
    n1.add_child(n2)
    n1.add_child(n3)

    expected = \
"""1
├── 2
|   └── 21
└── 3
"""

    result = n1.hierarchical_str()

    print(expected)
    print(len(expected))
    print(len(result))

    assert result == expected

def test_node_hierarchical_str_3_levels_2_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n21 = Node.create("21")
    n2.add_child(n21)
    n22 = Node.create("22")
    n2.add_child(n22)
    n3 = Node.create("3")
    n1.add_child(n2)
    n1.add_child(n3)

    assert n1.hierarchical_str() == \
"""1
├── 2
|   ├── 21
|   └── 22
└── 3
"""

def test_node_hierarchical_str_loop():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)
    n2.add_child(n1)

    assert n1.hierarchical_str() == \
"""1
└── 2
    └── 1
"""

def test_node_hierarchical_str_loop_2():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)
    n2.add_child(n1)
    n1.add_child(n1)

    assert n1.hierarchical_str() == \
"""1
├── 2
|   └── 1
└── 1
"""

def test_generate_n_node_levels_at_lest_max_depth(unique_node_names):
    levels = 3
    min_children = 1
    max_children = 10
    root_node = Node.create(list(unique_node_names)[0])
    generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children, deterministic_randrange)

    print(deterministic_randrange.all_rand_ints)
    print(root_node.hierarchical_str())
    # Check that max_depth is at least levels. It could be more than levels since a branch already created can be attached to a certain depth resulting beyond levels
    assert root_node.max_depth() >= levels

import os


@pytest.yield_fixture
def _3_levels_str():
    file_name = "fixture_50_nodes_3_levels_tree"
    yield next(load_levels_str(file_name))
#    return _load_levels_str("fixture_50_nodes_3_levels_tree")

@pytest.yield_fixture
def _6_levels_str():
    file_name = "fixture_5000_nodes_6_levels_tree"
    yield next(load_levels_str(file_name))
#    return _load_levels_str("fixture_50_nodes_3_levels_tree")

#def create_load_levels_str():
def load_levels_str(file_name):
    file_path = "%s/%s" % (os.path.dirname(os.path.abspath(__file__)), file_name)
    print(file_path)
    with open(file_path) as f:
        yield "".join(f.readlines())
# FIXME: code is not reaching here. This means f file is not being cleaned up.
    print("Tear down")
    assert False
 
#    return load_levels_str


def test_generate_n_node_levels_hierarchical_str(root_node_3_levels, _3_levels_str):
    root_node = root_node_3_levels
    hierarchical_str = root_node.hierarchical_str()
    print(deterministic_randrange.all_rand_ints)
    print(_3_levels_str)
    print(hierarchical_str)

    hierarchical_str_2 = root_node.hierarchical_str()
    assert hierarchical_str == hierarchical_str_2
    assert hierarchical_str == _3_levels_str

def test_get_node_with_index_path_invalid(root_node_3_levels):
    root_node = root_node_3_levels
    index_path = []
    result_node = root_node.get_node(index_path)

    assert result_node == None

def test_get_node_with_index_out_of_range(root_node_3_levels):
    root_node = root_node_3_levels
    index_path = [10]

    with pytest.raises(IndexError):
        root_node.get_node(index_path)

def test_get_node_with_index_path_0(root_node_3_levels):
    root_node = root_node_3_levels
    index_path = [0]
    result_node = root_node.get_node(index_path)

    assert result_node.name() == "generated_name_base_name_27"

def test_get_node_with_index_path_0_2(root_node_3_levels):
    root_node = root_node_3_levels
    index_path = [0, 2]
    result_node = root_node.get_node(index_path)

    assert result_node.name() == "generated_name_base_name_11"

def test_get_node_with_index_path_1_1_2_3(root_node_3_levels):
    root_node = root_node_3_levels
    index_path = [1, 1, 2, 3]
    result_node = root_node.get_node(index_path)

    assert result_node.name() == "generated_name_base_name_49"


# lazy traverse
# First apprach: lazy load a tree structure from a given in memory source tree

    # In Memory Fetch
@pytest.fixture
def in_memory_fetch(root_node_3_levels):
    def _in_memory_fetch(node, source_node=root_node_3_levels):
        node._children_dict = OrderedDict([(name,Node(name)) for name in source_node._children_dict])

    return _in_memory_fetch

@pytest.fixture
def lazy_root_node():
    root_node_name = "generated_name_base_name_20"
    root_node = Node(root_node_name)

    return root_node

@pytest.fixture
def lazy_root_node_6_levels():
    root_node_name = "generated_name_base_name_2039"
    root_node = Node(root_node_name)

    return root_node

def test_lazy_in_memory_fetch(lazy_root_node, in_memory_fetch):
    root_node = lazy_root_node

    assert not root_node.are_all_children_created()

    root_node.fetch(in_memory_fetch)
    n = len(root_node.children())
    root_children = list(root_node.children())

    assert n == 3
    assert root_node.are_all_children_created()
    assert root_children[0].name() == "generated_name_base_name_27"
    assert root_children[1].name() == "generated_name_base_name_21"
    assert root_children[2].name() == "generated_name_base_name_11"

def test_node_search_not_found(lazy_root_node_6_levels, in_memory_fetch):
    root_node = lazy_root_node_6_levels
    to_search = Node("not found")
    index_path = root_node.search(to_search, in_memory_fetch)

    assert index_path == []

def test_node_search_first_level(lazy_root_node_6_levels, in_memory_fetch):
    root_node = lazy_root_node_6_levels
    to_search = Node("generated_name_base_name_4938")

    index_path = root_node.search(to_search, in_memory_fetch)

    assert index_path == [0]

def test_node_search_second_level(lazy_root_node_6_levels, in_memory_fetch):
    root_node = lazy_root_node_6_levels
    to_search = Node("generated_name_base_name_124")

    index_path = root_node.search(to_search, in_memory_fetch)

    assert index_path == [0, 1]

def test_node_search_self(lazy_root_node_6_levels, in_memory_fetch):
    to_search = lazy_root_node_6_levels
    index_path = root_node.search(to_search, in_memory_fetch)

    assert index_path == [2, 2, 2, 4, 2]

def test_node_search_deep_level_and_repeated_node(lazy_root_node_6_levels, in_memory_fetch):
    root_node = lazy_root_node_6_levels
    to_search = Node("generated_name_base_name_4482")

    index_path = root_node.search(root_node, in_memory_fetch)

    assert index_path == [1, 1, 0, 1]

def test_parse_empty_tree():
    tree_str = "  "
    root_node = Node.parse_tree(tree_str)

    assert root_node == Node("")

def test_single_level_tree():
    tree_str = "1"
    root_node = Node.parse_tree(tree_str)
    
    assert root_node == Node(tree_str)

def test_single_3_levels_tree():
    tree_str = """1
├── 2
|   ├── 21
|   └── 22
└── 3
"""
    root_node = Node.parse_tree(tree_str)
    
    assert root_node.hierarchical_str() == tree_str

def test_6_levels_tree(_6_levels_str):
    root_node = Node.parse_tree(_6_levels_str)
    assert root_node.hierarchical_str() == _6_levels_str

def test_parse_lines_emtpy():
    lines = []
    
    node = Node._parse_lines(lines)
    assert not node

def test_parse_lines_root_node():
    lines = ["1"]
    
    node = Node._parse_lines(lines)
    assert node == Node("1")

def test_parse_lines_root_node():
    lines = ["1"]

    with pytest.raises(Node.SyntaxError):
        Node._parse_lines(lines, None, 1)

def test_parse_lines_root_node_with_not_none_parent_node():
    lines = ["1"]
    root_node = Node.create("0")

    with pytest.raises(Node.SyntaxError):
        Node._parse_lines(lines, root_node)

def test_parse_lines_first_level_multiple_children():
    tree_str = """1
└── 2
"""
    lines = ["├── 2"]
    root_node = Node.create("1")
    Node._parse_lines(lines, root_node, 1)
    
    assert root_node.hierarchical_str() == tree_str

def test_parse_lines_first_level_multiple_children_bad_current_level():
    lines = ["├── 2"]
    root_node = Node.create("1")

    with pytest.raises(Node.SyntaxError):
        # Sending current_level = 0 by default, should fail
        Node._parse_lines(lines, root_node)

def test_parse_lines_first_level_single_child():
    tree_str = """1
└── 2
"""
    lines = ["└── 2"]
    root_node = Node.create("1")
    Node._parse_lines(lines, root_node, 1)
    assert root_node.hierarchical_str() == tree_str

def test_parse_lines_first_level_bad_child_level():
    lines = ["    └── generated_name_base_name_49"]
    root_node = Node.create("1")

    with pytest.raises(Node.SyntaxError):
        Node._parse_lines(lines, root_node)

def test_parse_lines_single_3_levels_tree():
    tree_str = """2
└── 3
"""
    lines = ["└── 3"]
    first_child = Node.create("2")
    Node._parse_lines(lines, first_child, 1)
    
    assert first_child.hierarchical_str() == tree_str

def test_parse_line_root_level():
    line = "first level node"
    result = Node._parse_line(line)
    
    assert result[0] == 0
    assert result[1] == Node(line)
    assert result[2]

def test_parse_line_first_level():
    line = "├── First level node"
    result = Node._parse_line(line)
    
    assert result[0] == 1
    assert result[1] == Node("First level node")
    assert not result[2]

def test_parse_line_first_level():
    line = "└── First level node"
    result = Node._parse_line(line)
    
    assert result[0] == 1
    assert result[1] == Node("First level node")
    assert result[2]

def test_parse_line_first_level():
    line = "├── First level node"
    result = Node._parse_line(line)

    assert result[0] == 1
    assert result[1] == Node("First level node")
    assert not result[2]


def test_parse_line_second_level_1():
    line = "|   ├── Second level node"
    result = Node._parse_line(line)
    
    assert result[0] == 2
    assert result[1] == Node("Second level node")
    assert not result[2]

def test_parse_line_n_level_1():
    line = "    |   |   └── generated_name_base_name_17"
    result = Node._parse_line(line)
    
    assert result[0] == 4
    assert result[1] == Node("generated_name_base_name_17")
    assert result[2]
