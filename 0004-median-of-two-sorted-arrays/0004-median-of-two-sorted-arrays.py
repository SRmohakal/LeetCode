class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        helper = nums1 + nums2
        helper.sort()
        n = len(helper)
        if n % 2 == 0:
            return (helper[n//2 - 1] + helper[n//2]) / 2
        else:
            return helper[n//2]
