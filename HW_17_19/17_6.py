import sys
from functools import reduce

sys.setrecursionlimit(10000)

class Node: pass

make_node = lambda value: (lambda node: (setattr(node, "data", value), setattr(node, "left", None), setattr(node, "right", None), node)[-1])(Node())

insert = lambda self, node, value: make_node(value) if node is None else ((setattr(node, "left", self(self, node.left, value)), node)[1] if value < node.data else (setattr(node, "right", self(self, node.right, value)), node)[1])

preorder = lambda self, node: "" if node is None else node.data + self(self, node.left) + self(self, node.right)

lines = [line.strip() for line in sys.stdin.read().splitlines() if line.strip() != "*"]

root = reduce(lambda tree, symbol: insert(insert, tree, symbol), "".join(reversed(lines)), None)

print(preorder(preorder, root))

