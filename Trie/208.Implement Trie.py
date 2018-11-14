# Trie: use the common prefix to save the space
# The word is stored by "character by character" method

# 208. Implement Trie (Prefix Tree)
## This problem requires us to define the trie data structure

class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end = '/'

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for c in word:
            node[c] = node.get(c,{})
            node = node[c]
        node[self.end] = None

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        #print self.root
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self.end in node
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

