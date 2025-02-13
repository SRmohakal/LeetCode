from typing import List
from collections import deque

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        diagonals = {}

        for i in range(n):
            for j in range(n):
                d = i - j
                if d not in diagonals:
                    diagonals[d] = []
                diagonals[d].append(grid[i][j]) 

        for d in diagonals:
            if d >= 0:
                diagonals[d].sort(reverse=True) 
            else:
                diagonals[d].sort()  
            diagonals[d] = deque(diagonals[d])  

        for i in range(n):
            for j in range(n):
                d = i - j
                grid[i][j] = diagonals[d].popleft()  

        return grid
