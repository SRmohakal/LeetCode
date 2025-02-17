from collections import Counter
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backTrack(helper):
            total=0
            for char in helper:
                if helper[char]>0:
                    helper[char]-=1
                    total+=1+backTrack(helper)
                    helper[char]+=1
            return total

        return backTrack(Counter(tiles))