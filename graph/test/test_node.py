from node import Node

def test_url_correct_after_creation():
    link = "link"
    n = Node(link)
    assert n._url == link

def test_pointed_nodes_after_creation():
    n = Node("")
    assert n._pointed_nodes_set is not None

def test_pointed_by_nodes_after_creation():
    n = Node("")
    assert n._pointed_by_nodes_set is not None

def test_pointed_by_nodes_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_pointed_node(n2)
    assert n1 in n2._pointed_by_nodes_set

def test_pointed_nodes_after_add():
    n1 = Node("")
    n2 = Node("")
    n1.add_pointed_node(n2)
    assert n2 in n1._pointed_nodes_set
