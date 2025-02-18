class Solution:
    def smallestNumber(self, pattern: str) -> str:
        num=[]
        stack=[]

        for i in range(len(pattern)+1):
            stack.append(str(i+1))
            if i==len(pattern) or pattern[i]=='I':
                while stack:
                    num.append(stack.pop())

        return ''.join(num)

