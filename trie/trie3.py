class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Node()
            node = node.children[i]
        node.end = True

    def search(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.end

    def startwith(self,word):

        def _count(node,current,new):
            
            if node.end :
                new.append(current)
            for char,child in node.children.items():
                _count(child,current+char,new)
            return new
        node = self.root
        new = []
        for i in word:
            if i not in node.children:
                return []
            node = node.children[i]
        return _count(node,word,new)

    def collect_words(self, node=None, prefix="", words=None):
        """Collect all the words stored in the Trie."""
        if words is None:
            words = []
        if node is None:
            node = self.root

        if node.end:
            words.append(prefix)

        for char, child_node in node.children.items():
            self.collect_words(child_node, prefix + char, words)

        return words

obj = Trie()

obj.insert('hello')
obj.insert('hai')
obj.insert('hrnjjj')
# print(obj.collect_words())
# print(obj.search('hello'))
print(obj.startwith('ha'))
# print(obj.count_prefix('h'))