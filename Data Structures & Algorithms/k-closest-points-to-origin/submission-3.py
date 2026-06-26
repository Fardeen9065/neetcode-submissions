from math import sqrt
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        for lst in points:
            x = lst[0]
            y = lst[1]
            min_heap.append((sqrt(x**2+y**2),lst))
        heapq.heapify(min_heap)
        print(min_heap)
        ans = []
        for _ in range(k):
            x = heapq.heappop(min_heap)
            ans.append(x[1])
        return ans
        