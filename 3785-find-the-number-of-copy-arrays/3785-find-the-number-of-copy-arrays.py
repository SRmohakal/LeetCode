class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        n=len(original)
        min_val,max_val=bounds[0][0],bounds[0][1]

        for i in range(1,n):
            diff=original[i]-original[i-1]
            min_val=max(min_val+diff,bounds[i][0])
            max_val=min(max_val+diff,bounds[i][1])

            if min_val>max_val:
                return 0
        
        return (max_val-min_val+1)
        