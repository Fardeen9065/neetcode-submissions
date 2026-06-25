class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for num in stones:
            heapq.heappush(max_heap,-num)
        #print("max_heap:",max_heap)
        while len(max_heap) > 1:
            x = heapq.heappop(max_heap)
            y = heapq.heappop(max_heap)
            if y > x:
                heapq.heappush(max_heap,x-y)

            print(max_heap)
        if not max_heap:
            return 0
        return -max_heap[0]

        

        