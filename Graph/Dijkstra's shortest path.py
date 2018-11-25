"""
Dijkstra's shortest path algorithm
Given a graph and a source vertex, find the shortest path to all vertices in the graph.

Algorithm:
N is the number of vertices in the graph.
1. Set a length N All False list sptSet to record if the vertices has been considered.
2. Set a length N list to record the distance distance value from source to all vertice. 
Initialize the list by float('Inf') and forsource is 0.
3. Iterate the following steps N times:
   i. pick vertice u which is not in sptSet but has minimum distance value
   ii. add u into sptSet
   iii. update the distance values for all vertices v connected by u and v is not in sptSet.
    d[v] = min(d[v],d[u] + dist(u,v))
"""

##743. Network Delay Time
class Solution(object):
    def minIndex(self,dist,sptSet):
        minD,ans = float('inf'),0
        for i,d in enumerate(dist):
            if sptSet[i] == False and d < minD:
                minD = d
                ans = i
        return ans
    
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        graph = [[-1]*N for i in range(N)]
        for time in times:
            graph[time[0]-1][time[1]-1] = time[2]
        sptSet,dist = [False]*N,[float('Inf')]*N
        source = K-1
        dist[source] = 0
        for i in range(N):
            #print dist,sptSet
            sptSet[source] = True
            for i,d in enumerate(graph[source]):
                if d!= -1  and sptSet[i] != True:
                    dist[i] = min(dist[i],dist[source]+d)
            source = self.minIndex(dist,sptSet)
        res = max(dist)
        if res == float('inf'):
            return -1
        return res
        

   

