# 128. Longest Consecutive Sequence

## Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

## Your algorithm should run in O(n) complexity.

'''
The difficulty is the requirement of time complexity，we cannot compare each pair elements to check if it's consecutive.

My first idea is Union Find, the connection is (num,num+1) or (num-1,num). However I think it's not O(n) and 
 it does fail pass the last three cases.

Another idea is to find the maximum and minumum, when there is no duplicate number, if the max - min + 1 = length of array,
then the answer is max - min + 1. Based on the idea, I write a recursion function but it exceed the time.

Then I get a O(n) algorithm which need a large memory, we can create a zero array with length = max - min + 1. Then we 
go through the array, change the new array to 1 at the position num-min, then we calculate the maximum length of consecutive one 
in new array. However, it exceeds the memory.

The final idea is Hashing! Similar to the above idea, here we split the array into several parts and overlap them to avoid exceeding
the memory. This is hash! we build a hash map with maximum length equals to n, and project each number into a hash bucket such 
the consecutive numbers could fall into the consecutive bucket.

Here I just use (mod n) to finish hashing (n is the length of array, actucaly we should select a prime between n and 2n)
For each num in array, we should search from the consecutive bucket to find out its consecutive number.
To be mentioned, the consecutive bucket for the first bucket is the last one and the second one.
'''
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return n
        nums = list(set(nums))
        d,n = {},len(nums)
        for num in nums:
            if num%n in d:
                d[num%n].add(num)
            else:
                d[num%n] = set()
                d[num%n].add(num)
      
        ans,cur = 0,0
        f,l = min(d.keys()),max(d.keys())
        for num in nums:
            cur = 0
            if num in d[num%n]:
                cur = 1
                lkey,lvalue = num%n-1,num
                if lkey == f-1:
                    lkey = l
                rkey,rvalue = num%n+1,num
                if rkey == l+1:
                    rkey = f
                #find left side
                while lkey in d and lvalue-1 in d[lkey]:
                    cur += 1
                    d[lkey] -= set([lvalue-1])
                    lkey -=1
                    lvalue -=1
                    if lkey == f-1:
                        lkey = l
                    
                while rkey in d and rvalue+1 in d[rkey]:
                    cur += 1
                    d[rkey] -= set([rvalue+1])
                    rkey +=1
                    rvalue +=1
                    if rkey == l+1:
                        rkey = f
                ans = max(ans,cur)
            else:
                continue
        return ans
        