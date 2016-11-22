from node import Node

def test_url_correct_after_creation():
    link = "link"
    n = Node(link)
    assert n._url == link

def test_children_set_after_creation():
    n = Node("")
    assert n._children_set is not None

def test_pointed_by_nodes_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_child(n2)
    assert n2 in n1._children_set
