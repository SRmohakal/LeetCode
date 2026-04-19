class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0 
        max_dst = 0

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                max_dst = max(max_dst, j - i)
                j += 1
            else: 
                i += 1
        
        return max_dst