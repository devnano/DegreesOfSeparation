from node import Node
from node import *
import pytest

def setup_function(function):
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    Node._all_nodes = set()

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

# generation code test

@pytest.fixture
def unique_node_names():
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
    root_node = Node("")
    generate_node_random_names(root_node, unique_node_names, n)
    assert len(root_node._children_set) == n

# class methods

def test_node_get_all_nodes_set():
    all_nodes = Node.get_all_nodes()
    assert isinstance(all_nodes, set)

def test_node_all_nodes_len():
    root_node = Node("")
    all_nodes = Node.get_all_nodes()
    assert len(all_nodes) == 1

def test_node_all_nodes_len_n(unique_node_names):
    for name in unique_node_names:
        Node(name)
    all_nodes = Node.get_all_nodes()
    assert len(all_nodes) == len(unique_node_names)

def test_create_node_unique_instances():
    name = "unique_name"
    n1 = Node(name)
    n2 = Node(name)
    assert n1 == n2
    
