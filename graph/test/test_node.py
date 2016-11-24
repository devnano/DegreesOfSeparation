from node import Node
from node import *
import pytest

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    Node._all_nodes = dict()

def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function
    call.
    """

# core functionlality tests

def test_name_correct_after_creation():
    name = "name"
    n = Node(name)
    assert n._name == name

def test_children_set_after_creation():
    n = Node("")
    assert n._children_set is not None

def test_is_child_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_child(n2)
    assert n2 in n1._children_set

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

@pytest.fixture
def unique_node_names():
#    source_names = generate_unique_names(2000)
    source_names = {'generated_name_base_name_20', 'generated_name_base_name_17', 'generated_name_base_name_23', 'generated_name_base_name_38', 'generated_name_base_name_16', 'generated_name_base_name_27', 'generated_name_base_name_36', 'generated_name_base_name_49', 'generated_name_base_name_11', 'generated_name_base_name_21', 'generated_name_base_name_30', 'generated_name_base_name_10', 'generated_name_base_name_26', 'generated_name_base_name_6', 'generated_name_base_name_5', 'generated_name_base_name_4', 'generated_name_base_name_35', 'generated_name_base_name_40', 'generated_name_base_name_37', 'generated_name_base_name_25', 'generated_name_base_name_13', 'generated_name_base_name_22', 'generated_name_base_name_50', 'generated_name_base_name_43', 'generated_name_base_name_9', 'generated_name_base_name_8', 'generated_name_base_name_34', 'generated_name_base_name_41', 'generated_name_base_name_46', 'generated_name_base_name_29', 'generated_name_base_name_32', 'generated_name_base_name_18', 'generated_name_base_name_42', 'generated_name_base_name_28', 'generated_name_base_name_48', 'generated_name_base_name_44', 'generated_name_base_name_12', 'generated_name_base_name_19', 'generated_name_base_name_3', 'generated_name_base_name_45', 'generated_name_base_name_39', 'generated_name_base_name_7', 'generated_name_base_name_15', 'generated_name_base_name_47', 'generated_name_base_name_2', 'generated_name_base_name_31', 'generated_name_base_name_33', 'generated_name_base_name_24', 'generated_name_base_name_14'}
    return source_names

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
    root_node = Node.create(list(unique_node_names)[0])
    generate_node_random_names(root_node, unique_node_names, n)
    assert len(root_node.children()) == n

def test_depth_1p():
    n1 = Node.create("1")

    assert n1.depth() == 1

def test_depth_loop():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)
    n2.add_child(n1)

    assert n1.depth() == 2

def test_depth_2():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)

    assert n1.depth() == 2

def test_depth_3_multi_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n21 = Node.create("21")
    n22 = Node.create("22")
    n23 = Node.create("23")

    n1.add_child(n2)
    n2.add_child(n21)
    n2.add_child(n22)
    n2.add_child(n23)

    assert n1.depth() == 3

def test_depth_3_multi_child_on_each_level():
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

    assert n1.depth() == 3

def test_generate_n_node_levels(unique_node_names):
    levels = 2
    min_children = 1
    max_children = 10
    root_node = Node.create(list(unique_node_names)[0])
    generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children)
    assert len(root_node.children()) > 0 

def test_node_hierarchical_str_prefix_level_0():
    prefix = hierarchical_str_prefix(0, 0, 0)
    assert prefix == ""

def test_node_hierarchical_str_prefix_level_n_single_child():
    prefix = hierarchical_str_prefix(5, 0, 1)
    assert prefix == "└──"

def test_node_hierarchical_str_prefix_level_n_first_node_not_single_child():
    prefix = hierarchical_str_prefix(1, 0, 2)
    assert prefix == "├──"

def test_node_hierarchical_str_prefix_level_n_middle_child():
    prefix = hierarchical_str_prefix(3, 2, 5)
    assert prefix == "├──"

def test_node_hierarchical_str_prefix_level_n_last_child():
    prefix = hierarchical_str_prefix(3, 4, 5)
    assert prefix == "└──"

def test_node_hierarchical_str_single_level():
    n1 = Node.create("1")

    assert n1.hierarchical_str() == "1"

def test_node_hierarchical_str_2_levels_1_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n1.add_child(n2)

    assert n1.hierarchical_str() == \
"""1
   └──2"""

def test_node_hierarchical_str_2_levels_2_child():
    n1 = Node.create("1")
    n2 = Node.create("2")
    n3 = Node.create("3")
    n1.add_child(n2)
    n1.add_child(n3)

    assert n1.hierarchical_str() == \
"""1
   ├──2
   └──3"""

def test_generate_n_node_levels_depth(unique_node_names):
    levels = 3
    min_children = 1
    max_children = 10
    root_node = Node.create(list(unique_node_names)[0])
    generate_n_node_levels(root_node, unique_node_names, levels, min_children, max_children)
    print(root_node)
    assert root_node.depth() == levels
