"""
Brute Force: Run Time Limited
"""

class Solution(object):
    def isPalindrome(self,word):
        if len(word) == 0 or len(word) == 1:
            return True
        return word[0] == word[-1] and self.isPalindrome(word[1:-1])
    
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res,n = [],len(words)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if self.isPalindrome(words[i]+words[j]):
                        res.append([i,j])
        return res
"""
Trie:
"""

def isPalindrome(s):
    if len(s) < 2: return True
    return s[0] == s[-1] and isPalindrome(s[1:-1])
                                        
class Trie():
    def __init__(self):
        self.paths = {}
        self.end = -1
        self.PalindromeBelow = []
        
    def add(self,word,index):
        trie = self
        for i,char in enumerate(word[::-1]):
            if isPalindrome(word[:len(word)-i]):
                 trie.PalindromeBelow.append(index)
            trie.paths[char] = trie.paths.get(char,Trie())
            trie = trie.paths[char]
        trie.end = index


def SearchInTrie(word,trie,index):
    output = []
    for i,char in enumerate(word):
        if trie.end >= 0:
            if isPalindrome(word[i:]):
                output.append(trie.end)
        if char not in trie.paths:
            return output
        trie = trie.paths[char]
    if trie.end >= 0:
        output.append(trie.end)
    output += trie.PalindromeBelow
    return output

def palindromePairs(words):
    trie = Trie()
    for i,word in enumerate(words):
        trie.add(word,i)
    ans = []
    for i,word in enumerate(words):
        candidates = SearchInTrie(word,trie,i)
        ans +=  [[i,c] for c in candidates if c!= i]
    return ans


word = 'sssll'
t = Trie()
t.add(word,4)


t = t.paths['s']
print t.paths
print t.end
print t.PalindromeBelow
