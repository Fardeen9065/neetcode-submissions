class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lst in matrix:
            l = 0
            r = len(lst)-1
            while l <= r:
                mid = (l+r)//2
                if lst[mid] == target:
                    return True
                elif lst[mid] < target:
                    l += 1
                else:
                    r -= 1

        return False
        