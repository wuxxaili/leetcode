#287 Find the Duplicate Number

#Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
#prove that at least one duplicate number must exist. 
#Assume that there is only one duplicate number, find the duplicate one.

# time: O(n), space: O(1)
# [1,n] promise the 0 could be "head" in linked list, then we could use the method in 142
# function [0,n] ----> [1,n], where f(i) = A[i]
# exist (i,j) such f(i) = f(j), it will become a cycle

class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        fast,slow = 0,0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        slow2 = 0
        while slow2!=slow:
            slow2 = nums[slow2]
            slow = nums[slow]
        return slow
        