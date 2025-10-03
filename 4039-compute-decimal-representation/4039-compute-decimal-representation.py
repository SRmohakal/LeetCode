class Solution:
    def decimalRepresentation(self, n: int) -> List[int]:
        helper = []

        while n > 0:
            digit = n % 10
            helper.append(digit)
            n //= 10

        ans = []
        for i in range(len(helper)  -1 , -1, -1):
            if helper[i] != 0:
                current = helper[i] * (10**i)
                ans.append(current)
        
        return ans

