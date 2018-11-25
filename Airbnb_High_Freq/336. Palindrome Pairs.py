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