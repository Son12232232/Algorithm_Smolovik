import sys
from functools import reduce

data = sys.stdin.read().splitlines()
root = {}

[reduce(lambda node, name: node.setdefault(name, {}), path.split(chr(92)), root) for path in data[1:]]

print_tree = lambda node, depth: [(print(" " * depth + name), print_tree(node[name], depth + 1)) for name in sorted(node)]

print_tree(root, 0)
