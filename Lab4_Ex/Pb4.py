import operator
import matplotlib.pyplot as plt
import networkx as nx

class ASTNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_ast(tokens):
    ops = {
        '+': (1, operator.add),
        '-': (1, operator.sub),
        '*': (2, operator.mul),
        '/': (2, operator.truediv)
    }

    values = []
    operators = []

    def apply_operator():
        op = operators.pop()
        right = values.pop()
        left = values.pop()
        values.append(ASTNode(op, left, right))

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token.isdigit():
            values.append(ASTNode(int(token)))
        elif token in ops:
            while (operators and operators[-1] in ops and 
                   ops[operators[-1]][0] >= ops[token][0]):
                apply_operator()
            operators.append(token)
        i += 1

    while operators:
        apply_operator()

    return values[0]

def eval_ast(node):
    if isinstance(node.value, int):
        return node.value
    left_val = eval_ast(node.left)
    right_val = eval_ast(node.right)
    if node.value == '+':
        return left_val + right_val
    elif node.value == '-':
        return left_val - right_val
    elif node.value == '*':
        return left_val * right_val
    elif node.value == '/':
        return left_val / right_val

def add_edges_ast(graph, node, parent=None):
    if node is None:
        return
    graph.add_node(node.value)
    if parent:
        graph.add_edge(parent.value, node.value)
    add_edges_ast(graph, node.left, node)
    add_edges_ast(graph, node.right, node)

expression = "13*2-11+5+21/7"
tokens = ['13', '*', '2', '-', '11', '+', '5', '+', '21', '/', '7']
ast_root = build_ast(tokens)

result = eval_ast(ast_root)

graph = nx.DiGraph()
add_edges_ast(graph, ast_root)

plt.figure(figsize=(10, 8))
pos = nx.spring_layout(graph)
nx.draw(graph, pos, with_labels=True, arrows=False, node_size=3000, node_color="lightblue", font_size=12, font_weight="bold")
plt.title("AST Visualization")
plt.show()


