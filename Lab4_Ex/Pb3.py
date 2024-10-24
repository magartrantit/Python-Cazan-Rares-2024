import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root, result=None):
    if result is None:
        result = []
    if root:
        inorder_traversal(root.left, result)
        result.append(root.val)
        inorder_traversal(root.right, result)
    return result

def add_edges(graph, root):
    if root is None:
        return
    if root.left:
        graph.add_edge(root.val, root.left.val)
        add_edges(graph, root.left)
    if root.right:
        graph.add_edge(root.val, root.right.val)
        add_edges(graph, root.right)

def hierarchy_pos(root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5):
    pos = _hierarchy_pos(root, width, vert_gap, vert_loc, xcenter)
    return pos

def _hierarchy_pos(root, width=1., vert_gap = 0.2, vert_loc = 0, xcenter = 0.5, pos=None, parent=None, left_right=True):
    if pos is None:
        pos = {root.val: (xcenter, vert_loc)}
    else:
        pos[root.val] = (xcenter, vert_loc)
    if root.left is not None:
        nextx = xcenter - width/2 
        pos = _hierarchy_pos(root.left, width/2, vert_gap, vert_loc-vert_gap, nextx, pos, root, True)
    if root.right is not None:
        nextx = xcenter + width/2  
        pos = _hierarchy_pos(root.right, width/2, vert_gap, vert_loc-vert_gap, nextx, pos, root, False)
    return pos

elements = [50, 30, 70, 20, 40, 60, 80, 10, 90, 5, 100, 2, 7, 1, 3]
bst_root = None
for element in elements:
    bst_root = insert(bst_root, element)


inorder_result = inorder_traversal(bst_root)

graph = nx.DiGraph()
add_edges(graph, bst_root)

plt.figure(figsize=(10, 8))
pos = hierarchy_pos(bst_root)
nx.draw(graph, pos, with_labels=True, arrows=False, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold")
plt.title("BST Visualization")
plt.show()
