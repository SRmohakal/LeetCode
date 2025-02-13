class Solution:
    def findValidPair(self, s: str) -> str:
        ans = []
        for i in range(len(s) - 1):  
            if s[i] != s[i + 1] and s.count(s[i]) == int(s[i]) and s.count(s[i + 1]) == int(s[i + 1]):
                ans.append(s[i])
                ans.append(s[i + 1])
        
        if len(ans) > 2:
            return "".join(ans[:2])  
        
        return "".join(ans)  
