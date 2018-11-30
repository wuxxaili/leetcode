"""
269. Alien Dictionary

There is a new alien language which uses the latin alphabet. However, the order among letters 
are unknown to you. You receive a list of non-empty words from the dictionary, where words are 
sorted lexicographically by the rules of this new language. Derive the order of letters in this language.
"""

"""
Idea: for two words, compare their letters one by one. Find the first index i that they have
different letter, then we will know s2[i] > s1[i]. We could construct a graph let s1[i] -> s2[i].
After we construct all the graphs. Then 1. find the letters that no other letters point to, it will be 
the smallest letters. 2. Delete all the letters in the first step from the graph and repeat step1.

Be careful, if (a,b) was deleted due to a, b might also disapper in the graph, we need also add b.
"""

def alienOrder(words):
    d = {}
    All_letters = set(words[0])
    for i in range(1,len(words)):
        All_letters |= set(words[i])
        for l1,l2 in zip(words[i-1],words[i]):
            if l1 != l2:
                d[l2] = d.get(l2,set()) | set([l1])
                d[l1] = d.get(l1,set())
                break
    ans = list(All_letters - set(d.keys())
    while d:
        letters = d.keys()
        small = set()
        for l in letters:
            if d[l] == set():
                small.add(l)
                del d[l]
        if small == set():
            return '' 
        for l in d:
            d[l] -= small
        ans += list(small)
    return ''.join(ans)