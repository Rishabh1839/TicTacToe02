import numpy as np

np.array([1, 3, 5, 7])
A = np.mat([[1, 2], [3, 3]])
A + A
A - A
A * A
np.linalg.det(A)
np.matrix.transpose(A)

A = np.mat([4, 5, 6], [1, 2, 3], [7, 8, 9])

root = {'value': 1, 'depth': 1}


def succ(node):
    if node['value'] == 5:
        return []
    elif node['value'] == 4:
        return [{'value': 5, 'depth':
            node['depth'] + 1}]
    else:
        return [
            {'value': node['value'] + 1,
             'depth': node['depth'] + 1},
            {'value': node['value'] + 2,
             'depth': node['depth'] + 1}
        ]


def bfs_tree(node):
    nodes_to_visit = [node]
    visited_nodes = []
    while len(nodes_to_visit) > 0:
        current_node = nodes_to_visit.pop(0)
        visited_nodes.append(current_node)
        nodes_to_visit.extend(succ(current_node))
        return visited_nodes
    bfs_tree(root)
