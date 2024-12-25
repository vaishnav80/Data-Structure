class Node:
    def __init__(self):
        self.children = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = Node()
    