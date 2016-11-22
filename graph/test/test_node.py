from node import Node
from node import *

def test_url_correct_after_creation():
    link = "link"
    n = Node(link)
    assert n._url == link

def test_children_set_after_creation():
    n = Node("")
    assert n._children_set is not None

def test_is_child_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_child(n2)
    assert n2 in n1._children_set

# generation code test

def test_generate_link_name():
    link_name = generate_link_name(1)
    assert "generated_link_base_name_1" == link_name

def test_generate_unique_links_len():
    n = 100
    unique_links = generate_unique_links(n)
    assert len(unique_links)

def test_generate_unique_links_type():
    n = 1
    unique_links = generate_unique_links(n)
    assert isinstance(unique_links, set)
