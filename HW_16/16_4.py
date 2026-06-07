import sys

class Node: pass

def minimum_fee(node): return node.fee if not node.children else node.fee + min(minimum_fee(child) for child in node.children)

n = int(sys.stdin.readline())

rows = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

nodes = [Node() for _ in range(n)]

def prepare(i): nodes[i].fee = rows[i][0]; nodes[i].children = []

[prepare(i) for i in range(n)]

def connect(i): nodes[i].children = [nodes[number - 1] for number in rows[i][2:]]

[connect(i) for i in range(n)]

print(minimum_fee(nodes[0]))
