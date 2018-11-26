"""
Find Median in average O(n)
https://rcoh.me/posts/linear-time-median-finding/

Use the algorithm similar to Quick Sort.
1. select the pivot randomly
2. split the array into two partuse pivot, compare their length
3. repeat step 1 and 2 on the longer array
"""
import random
def QuickSelect(nums,k):
    ## select kth element in nums
    small,large,pivot = [],[],[]
    pivot_num = nums[random.randint(0,len(nums)-1)]
    for num in nums:
        if num < pivot_num:
            small.append(num)
        elif num == pivot_num:
            pivot.append(num)
        else:
            large.append(num)
    if len(small) > k:
        return QuickSelect(small,k)
    elif len(small) + len(pivot) > k:
        return pivot_num
    else:
        return QuickSelect(large,k - len(small) - len(pivot))

def QuickMedian(nums):
    n = len(nums)
    if n % 2 == 1:
        return QuickSelect(nums,n//2)
    else:
        return (QuickSelect(nums,n//2 - 1) + QuickSelect(nums,n//2))/2.0


"""
AIRBNB : Find Median in Large Integer File of Integers
    
Find the median from a large file of integers. You can not access the numbers by index, can only access it sequentially. And the numbers cannot fit in memory.

Idea:
Using binary search, first scan it to find min and max, then the guess for median should be (min + max)//2. Scan the file again to count the number under guess and over guess. Accoriding to the length move the min/max, re-guess the median and repeat the steps.
"""
nums = [3, 4, 2, 5, 7, 9, 10, 14, 11, 5, 7]
def KthBinarySearch(nums,k,MAX,MIN,LMAX,LMIN):
    ## return the kth element in nums
    if MIN == MAX: return MIN
    #print k,MAX,MIN,LMAX,LMIN
    median = (MIN + MAX)//2
    s,l,m = 0,0,0
    for num in nums:
        if LMIN <= num <= LMAX:
            if num < median:
                s += 1
            elif num == median:
                m += 1
            else:
                l += 1
    if s > k:
        return KthBinarySearch(nums,k,median-1,MIN,median-1,LMIN)
    if s + m > k:
        return median
    else:
        return KthBinarySearch(nums,k - s - m,MAX,median+1,LMAX,median+1)

def MedianBinarySearch(nums):
    MIN,MAX = float('Inf'),-float('Inf')
    n = 0
    for num in nums:
        n += 1
        MIN = min(num,MIN)
        MAX = max(num,MAX)
    if n == 2: return 0.5*(MIN + MAX)
    if n % 2 == 1:
        return KthBinarySearch(nums,n/2,MAX,MIN,MAX,MIN)
    else:
        return 0.5*(KthBinarySearch(nums,n/2,MAX,MIN,MAX,MIN) + KthBinarySearch(nums,n/2-1,MAX,MIN,MAX,MIN))
