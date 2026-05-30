class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        ans = []

        for i in strs:
            if str(sorted(i)) not in hash_map:
                hash_map[str(sorted(i))] = [i]
            else:
                hash_map[str(sorted(i))].append(i)

        for i in hash_map.values():
            ans.append(i)
        return ans

        