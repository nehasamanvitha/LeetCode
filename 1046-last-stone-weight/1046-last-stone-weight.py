import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap=[]
        heap=[-x for x in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)
            if x!=y:
                heapq.heappush(heap,-(x-y))
        return -heap[0] if heap else 0
        
        