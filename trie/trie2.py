class Trienode:
    def __init__(self):
        self.children={}
        self.end = False


class Trie:
    def __init__(self):
        self.root = Trienode()

    def insert(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Trienode()
            node = node.children[char]
        node.end = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end
    
    def startwith(self,prefix):

        def _count(node,current):
            
            word = []
            if node.end:
                word.append(current)
            
            for char,child in node.children.items():
                
                word.extend(_count(child,current+char))
            return word

        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        return _count(node,prefix)
    
    def count(self):
        def _count(node):
            count = 1 if node.end else 0
            for child in node.children.values():
                count += _count(child)
            return count

        return _count(self.root)
    
    def count_prefix(self,prefix):
        def _count(node):
            count = 1 if node.end else 0
            
            for child in node.children.values():
                # print(node.children)
                count += _count(child)
            return count
        
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return _count(node)
        
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
print(obj.collect_words())
print(obj.search('hel'))
print(obj.startwith('h'))
print(obj.count_prefix('h'))
