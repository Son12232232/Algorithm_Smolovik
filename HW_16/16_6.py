import sys

sys.setrecursionlimit(5000)

class Node: pass

lines = sys.stdin.read().splitlines()
n = int(lines[0])

nodes = [Node() for _ in range(n)]
[(setattr(node, "children", []), setattr(node, "value", None)) for node in nodes]

rows = [line.split() for line in lines[1:]]

[(nodes[int(row[1]) - 1].children.append(nodes[i]), setattr(nodes[i], "value", int(row[2])) if row[0] == "L" else None) for i, row in enumerate(rows, 1)]

game_result = lambda self, node, first_turn: node.value if node.value is not None else (max if first_turn else min)(self(self, child, not first_turn) for child in node.children)

answer = game_result(game_result, nodes[0], True)

print("+1" if answer == 1 else answer)
