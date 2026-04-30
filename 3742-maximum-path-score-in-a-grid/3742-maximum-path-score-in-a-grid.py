class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n = len(grid), len(grid[0])

        dp = [[{} for _ in range(n)] for _ in range(m)]
        dp[0][0] = {0:0}

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = grid[i][j]
                cost = 0 if val == 0 else 1
                score = val
                curr = {}

                for pi, pj in [(i-1, j), (i, j-1)]:
                    if pi < 0 or pj < 0:
                        continue
                    
                    for c_prev, s_prev in dp[pi][pj].items():
                        new_cost = c_prev + cost
                        if new_cost > k:
                            continue
                        
                        new_score = s_prev + score
                        
                        if new_cost not in curr or curr[new_cost] < new_score:
                            curr[new_cost] = new_score
                
                items = sorted(curr.items())
                pruned = {}
                max_score_so_far = -1
                
                for c, s in items:
                    if s > max_score_so_far:
                        pruned[c] = s
                        max_score_so_far = s
                
                dp[i][j] = pruned
        
        if not dp[m-1][n-1]:
            return -1
        
        return max(dp[m-1][n-1].values())

