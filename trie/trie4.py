class Node :
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
    
    def prefix(self,word):

        def count(node,word,new):
            if node.end:
                
                new.append(word)
            
            for k,v in node.children.items():
                count(v,word+k,new)
            return new

        node = self.root
        new = []
        for i in word:
            if i not in node.children:
                return []
            node = node.children[i]
        return count(node,word,new)
    
    def collect(self,node=None,prefix = " ",word = None):
        if word is None:
            word = []

        if node is None:
            node = self.root 

        if node.end:
            word.append(prefix)

        for k,v in node.children.items():
            self.collect(v,prefix+k,word)

        return word
    
obj = Trie()
obj.insert('hello')
obj.insert('hai')
print(obj.collect())
print(obj.prefix('h'))
print(obj.search('hai'))
        
        