class Trienode:
    def __init__(self):
        self.children = {}
        self.end = False

    
class Trie:
    def __init__(self):
        self.root = Trienode()
    
    def insert(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                node.children[i] = Trienode()
            node = node.children[i]
        
        node.end =True


    def search(self,word):
        node = self.root
        for i in word:
            if i not in node.children:
                return False
            node = node.children[i]
        return node.end


    # def collect_words(self, node=None, prefix="", words=None):
    #     """Collect all the words stored in the Trie."""
    #     if words is None:
    #         words = []
    #     if node is None:
    #         node = self.root

    #     if node.end:
    #         words.append(prefix)

    #     for char, child_node in node.children.items():
    #         self.collect_words(child_node, prefix + char, words)

    #     return words
    def find_words_with_prefix(self, prefix):
        current_node = self.root
        result = []

        # Traverse to the end of the prefix
        for char in prefix:
            if char not in current_node.children:
                return []  # If prefix not found, return empty list
            current_node = current_node.children[char]

        # Call the helper function to collect all words starting from the end of the prefix
        self._collect_words(current_node, prefix, result)
        return result

    # Helper function to collect all words from a given node
    def _collect_words(self, node, prefix, result):
        if node.end:
            result.append(prefix)

        for char, child_node in node.children.items():
            self._collect_words(child_node, prefix + char, result)

    

obj = Trie()

obj.insert('hello')
obj.insert('hai')
# print(obj.collect_words())
print(obj.search('haisdf'))
print(obj.find_words_with_prefix('he'))