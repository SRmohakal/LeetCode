class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        ans = []
        for val in order:
            if val in friends:
                ans.append(val)
        
        return ans 