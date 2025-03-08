class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_op = blocks[:k].count('W')
        temp_op = min_op
        
        for i in range(k, len(blocks)):
            if blocks[i-k] == 'W':
                temp_op -= 1
    
            if blocks[i] == 'W':
                temp_op += 1
            
            min_op = min(min_op, temp_op)

        return min_op