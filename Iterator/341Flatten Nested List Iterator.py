#Similar as 251

#Given a nested list of integers, implement an iterator to flatten it.

#Each element is either an integer, or a list -- whose elements may also be integers or other lists.

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        
    def next(self):
        """
        :rtype: int
        """
        return self.nestedList.pop(0).getInteger()
        

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.nestedList:
            f = self.nestedList[0]
            if f.isInteger():
                return True
            self.nestedList = f.getList() + self.nestedList[1:] 
        return False
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
