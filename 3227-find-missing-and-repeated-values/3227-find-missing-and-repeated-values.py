class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n=len(grid)*len(grid[0])

        expected_sum=n*(n+1)//2
        expected_sum_of_squares=(n*(n+1)*(2*n+1))//6

        actual_sum=0
        actual_sum_of_squares=0
        for row in grid:
            for num in row:
                actual_sum+=num
                actual_sum_of_squares+=num*num

        b_a=expected_sum - actual_sum #b−a
        bb_aa=expected_sum_of_squares -actual_sum_of_squares #b^2-a^2

        sum_ab=bb_aa//b_a #b+a
        b=(sum_ab+b_a)//2 #(b+a + b-a)=2b
        a=sum_ab-b #(b+a -b)=a
        return [a, b]


        