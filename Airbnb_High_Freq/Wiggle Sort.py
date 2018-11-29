"""
Wiggle sort II
"""

def wiggleSort(nums):
        n = len(nums)
        median = MedianBinarySearch(nums) #First find median o(n),o(1)
        s = (n - 1) / 2 * 2 # position for the small number,begin with last even index
        l = 1#position for the large number
        i = 0
        while i < n:
            if num[i] > median:
                if i%2 == 1 and i <= l: c
                    i += 1
                    continue #skip the elements which already checked
                swap(nums,l,i)
                l += 2
            elif nums[i] < median:
                if i%2 == 0 and i >= s: 
                    i += 1
                    continue 
                swap(nums,s,i)
                s -= 2
            else:
                i += 1
            
def swap(nums,i,j):
    tem = nums[i]
    nums[i] = nums[j]
    nums[j] = tem
            
            
            
def KthBinarySearch(nums,k,MIN,MAX):
    while MIN <= MAX:
        guess,nextLarge = (MIN + MAX)/2,MAX
        s,m = 0,0
        for num in nums:
            if num < guess:
                s += 1
            elif num == guess:
                m += 1
            else:
                nextLarge = min(num,nextLarge)
        if s > k :
            MAX = guess - 1
            continue
        if s+m > k :
            return guess
        if s+m == k:
            return nextLarge
        else:
            MIN = guess + 1

def MedianBinarySearch(nums):
    MIN,MAX = min(nums),max(nums)
    n = len(nums)
    if n % 2 == 1:
        return KthBinarySearch(nums,n/2,MIN,MAX)
    else:
        return 0.5*(KthBinarySearch(nums,n/2,MIN,MAX) + KthBinarySearch(nums,n/2-1,MIN,MAX))


#def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        
        from heapq import *
        n = len(nums)
        maxH = [-x for x in nums]
        heapify(maxH)
        for i in range(1,n,2):
            nums[i] = -heappop(maxH)
        for i in range(0,n,2):
            nums[i] = -heappop(maxH)
        """
