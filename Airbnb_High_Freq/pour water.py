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
                    