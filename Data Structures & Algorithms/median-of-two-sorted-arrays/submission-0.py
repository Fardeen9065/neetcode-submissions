class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = sorted(nums1+nums2)
        
        if len(nums) % 2 == 1:
            l,r = 0,len(nums)-1
            m = (l+r)//2
            return nums[m]
        else:
            l,r = 0,len(nums)-1
            m = (l+r)//2
            return (nums[m] + nums[m+1])/2

            
        