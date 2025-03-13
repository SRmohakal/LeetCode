import heapq
class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        n = len(nums1)
        indexed_nums = sorted(enumerate(nums1), key=lambda x: x[1])  
        ans = [0] * n
        max_heap = []  
        total = 0  
        j = 0  

        for i, val in indexed_nums:
            while j < n and indexed_nums[j][1] < val:
                idx = indexed_nums[j][0]
                heapq.heappush(max_heap, nums2[idx])  
                total += nums2[idx] 
                if len(max_heap) > k:
                    total -= heapq.heappop(max_heap)  
                j += 1

            ans[i] = total

        return ans