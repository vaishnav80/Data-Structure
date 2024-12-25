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
    

    def collect(self,node = None,word = None,prefix = " "):
        if word is None:
            word  = []
        if node is None:
            node = self.root
        if node.end:
            word.append(prefix)
        
        for k,v in node.children.items():
            print(k,v)
            self.collect(v,word,prefix+k)
        return word
    
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
    
    def search(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.end
    
    def prefix2(self,word):

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


    def collect2(self,node = None,word = "",new = None,count=0):
        if node is None:
            node = self.root
        if new is None:
            new = {}
        if node.end:
            new[word] = count
            count = 0
        for k,v in node.children.items():
            count+=1
            self.collect2(v,word+k,new,count)
        # length = " "
        # for i in new:
        #     count = len(i)
        #     if count >len(length) :
        #         length = i
        return new,max(new)
    
    def delete(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                return None
            node = node.children[i]
        node.end = False
    
obj = Trie()
obj.insert('hai')
obj.insert('hello')
print(obj.collect2())
print(obj.prefix2('ha'))
print(obj.search('haid'))
# obj.delete('hai')
print(obj.collect2())
