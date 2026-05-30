class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        lst = set()

        for i in nums:
            if i not in lst:
                lst.add(i)
            else:
                return True

        return False
        