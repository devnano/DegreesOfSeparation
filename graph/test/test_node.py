from node import Node

def test_add_pointed_node():
    n = Node("")
    assert len(n.pointed_nodes_set) == 0
