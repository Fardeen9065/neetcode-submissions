class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            if i not in hash_map:
                hash_map[i] = 1
            else:
                hash_map[i] += 1
        
        arr = []
        for num,cnt in hash_map.items():
            arr.append([cnt,num])
        arr.sort()
        res = []
        for i in range(k):
            res.append(arr.pop()[1])
        return res

        