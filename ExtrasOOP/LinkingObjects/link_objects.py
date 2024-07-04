# Link Objects


data = [[3, False], [4, True], [5, False],
        [6, True], [7, False], [8, True]]


class Node:

    def __init__(self, value, parent_node, allowance):
        self.value = value
        self.allowance = allowance
        self.parent_node = parent_node


class Solution:

    def __init__(self, current_data):
        self.current_data = current_data
        self.nodes_collection: list[Node] = []

    def add_node(self, data_piece, parent_node):
        self.nodes_collection.append(Node(data_piece[0], data_piece[1], parent_node))




print("New")
print("New2")
print("New 3")
print("New 4")
print("New 5")
print("New 6")
print("New 7")
print("New 8")
print("New 9")
print("New 10")
print("New 11")
print("New 12")
print("New 13")
print("New 14")
print("New 15")
