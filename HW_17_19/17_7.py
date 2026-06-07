import sys

class TreeNode: pass
class Tree: pass

make_node = lambda value: (lambda node: (setattr(node, "val", value), setattr(node, "left", None), setattr(node, "right", None), node)[-1])(TreeNode())

insert = lambda self, node, value: make_node(value) if node is None else ((setattr(node, "left", self(self, node.left, value)), node)[1] if value < node.val else (setattr(node, "right", self(self, node.right, value)), node)[1])

same = lambda self, first, second: True if first is None and second is None else False if first is None or second is None else first.val == second.val and self(self, first.left, second.left) and self(self, first.right, second.right)

Tree.Insert = lambda self, value: setattr(self, "head", insert(insert, self.head, value))
Tree.IsSameTree = lambda self, other: 1 if same(same, self.head, other.head) else 0

data = list(map(int, sys.stdin.buffer.read().split()))

n = data[0]
m_position = n + 1
m = data[m_position]

first_tree = Tree()
first_tree.head = None

second_tree = Tree()
second_tree.head = None

[first_tree.Insert(value) for value in data[1:n + 1]]
[second_tree.Insert(value) for value in data[m_position + 1:m_position + 1 + m]]

print(first_tree.IsSameTree(second_tree))
