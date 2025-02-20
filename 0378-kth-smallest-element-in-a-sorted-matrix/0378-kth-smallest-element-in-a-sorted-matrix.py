class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n=len(matrix)
        ans=[]

        for i in range(n):
            for j in range(n):
                ans.append(matrix[i][j])

        ans.sort()
        return ans[k-1]