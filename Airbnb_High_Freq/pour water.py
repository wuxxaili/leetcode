def pourWater(heights, V, K):
    n = len(heights)
    for _ in range(V):
        print heights
        index = K    
        for i in range(K-1,-1,-1):
            if heights[i] > heights[i+1]:
                break
            if heights[i] < heights[i+1]:
                index = i
        if index != K:
            heights[index] += 1
            continue
        for i in range(K+1,n):
            if heights[i-1] < heights[i]:
                break
            if heights[i-1] > heights[i]:
                index = i
        heights[index] += 1
    return heights

"""
## print the land
nums = [2,1,2,1,3]
newnums = [2,2,2,2,3]
n = len(nums)

maxHeight = max(newnums)
for height in range(maxHeight,0,-1):
    row = ''
    for j in range(n):
        if newnums[j] >= height and nums[j] < height:
            row += 'w'
        elif nums[j] >= height:
            row += '+'
        else:
            row += ' '
    print row
"""
