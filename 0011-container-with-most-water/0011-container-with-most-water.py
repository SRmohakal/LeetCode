class Solution:
    def maxArea(self, height: List[int]) -> int:
        lf,rt=0,len(height)-1
        max_water=0

        while lf<rt:
            h=min(height[lf],height[rt])
            max_water=max(max_water,h*(rt-lf))

            if height[lf]<height[rt]:
                lf+=1
            else:
                rt-=1
        
        return max_water