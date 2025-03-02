class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        values={}

        for id1,val1 in nums1:
            values[id1]=values.get(id1,0)+val1
        
        for id2,val2 in nums2:
            values[id2]=values.get(id2,0)+val2

        ans=[[id,val] for id,val in sorted(values.items())]
        return ans