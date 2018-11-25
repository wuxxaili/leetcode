"""
41. First Missing Positive

Given an unsorted integer array, find the smallest missing positive integer.
Time: O(n)
Space: O(1)
"""

"""
Initial idea is to change the list in-place (like multiply the indexed number -1 to denote we have met this value).
However in this problem the list will have negative number.
First I came up with a space O(n) algorithm, use a new vector to denote if we have met before.
From the discussion I know we can simply swap the num and nums[num-1], which means putting the number into the correct position.
Then we can check the missing value by go through the list again.
One trick is we need temporary variable to swap.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n,i = len(nums),0
        while i < 0:
            # ignore the number out of the range
            if 0 < nums[i] <= n:
                if nums[i] != nums[num[i]-1]:
                    tem = nums[i]
                    nums[i] = nums[tem-1] 
                    nums[tem-1] = tem
                    continue
            i += 1
        for i in range(n):
            if i+1 != nums[i]:
                return i + 1
        return n + 1