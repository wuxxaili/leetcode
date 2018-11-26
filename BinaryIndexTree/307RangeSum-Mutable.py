"""
Binary Indexed Tree

Two target:
1. Find the sum from index i to j
2. Update the value at index i

Time Complexity: Sum:O(logn), Update: O(logn)

Suppose the length of array is n. Build an array BIT[] with same length. (In python build array with
n+1 length will be more easier)

BIT[x] = a[x] if x is odd
BIT[x] = a[1] + ... + a[x] if x in power of 2
BIT[x] = a[x-r+1] + .. + a[x] here r = x&-x, last set bit in x

when we update x, we need to update all the BIT contains a[x]
while x < n:
    update BIT[x]
    x += x&-x

when we calculate sum form 1 to x:
ans = 0
while x > 0:
    ans += BIT[x]
    x -= x&-x
"""

#307. Range Sum Query - Mutable

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.n = len(nums)
        self.BIT = [0]*(self.n+1)
        for i in range(1,self.n+1):
            j = i 
            while j < self.n + 1:
                self.BIT[j] += nums[i-1]
                j += j &(-j)
        self.nums = nums
        
    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        change = val - self.nums[i]
        self.nums[i] = val
        i = i+1
        while i < self.n + 1:
            self.BIT[i] += change
            i += i&-i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        ans1,ans2 = 0,0
        x1,x2 = j + 1, i
        while x1 > 0:
            ans1 += self.BIT[x1]
            x1 -= x1&-x1
        while x2 > 0:
            ans2 += self.BIT[x2]
            x2 -= x2 &-x2
        return ans1 - ans2
        