from collections import Counter, deque
import heapq
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        freq = Counter(tasks)

        heap = [-count for count in freq.values()]
        heapq.heapify(heap)
        cooldown = deque()

        time = 0

        while heap or cooldown:
            time += 1
            if heap:
                count = heapq.heappop(heap)
                count += 1 

                if count != 0:
                    cooldown.append((count, time + n))
            if cooldown and cooldown[0][1] == time:
                count, _ = cooldown.popleft()
                heapq.heappush(heap, count)

        return time