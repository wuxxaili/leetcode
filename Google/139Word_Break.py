"""
139. Word Break


"""

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False]*n
        for i in range(n):
            for word in wordDict:
                if word == s[i-len(word)+1:i+1] and (dp[i-len(word)] or i+1 ==len(word)):
                    dp[i] = True    
        return dp[n-1]
        
        
"""
140. Word Break II


"""
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        dp = [False]*n
        d = {}
        for i in range(n):
            for w in wordDict:
                if w == s[i+1-len(w):i+1] and (dp[i-len(w)] or len(w) == i+1):
                    dp[i] = True
                    d[i] = d.get(i,[]) + [w]

        if n-1 not in d: return []
        def dfs(ans,k):
            if k < 0: return ans
            res = []
            for c in d[k]:
                newans = []
                for succ in ans:
                    newans.append(c+ ' ' +succ)
                res += dfs(newans,k-len(c))
            return res
        ans = []
        for w in d[n-1]:
            ans += dfs([w],n-1-len(w))
        return ans