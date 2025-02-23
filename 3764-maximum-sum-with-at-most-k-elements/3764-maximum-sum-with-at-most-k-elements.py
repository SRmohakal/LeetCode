class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        ans = []
        
        for row, limit in zip(grid, limits):
            ans.extend(sorted(row, reverse=True)[:limit])
        ans.sort(reverse=True)
        
        return sum(ans[:k])