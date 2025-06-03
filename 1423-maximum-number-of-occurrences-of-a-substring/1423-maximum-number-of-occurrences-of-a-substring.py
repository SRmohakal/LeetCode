class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        f=defaultdict(int)
        max_occur=0

        for i in range(len(s)-minSize+1):
            sub_str=s[i:i+minSize]
            unique=set(sub_str)
            if len(unique)<=maxLetters:
                f[sub_str]+=1
                max_occur=max(max_occur,f[sub_str])
                
        return max_occur
                
        