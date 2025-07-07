import heapq
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() 
        min_heap = []
        i = 0
        n = len(events)
        res = 0

        max_day = max(e[1] for e in events)

        for day in range(1, max_day + 1):
            while i < n and events[i][0] == day:
                heapq.heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                res += 1

        return res
