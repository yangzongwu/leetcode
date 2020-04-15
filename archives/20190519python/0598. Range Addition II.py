class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row=m
        min_col=n
        for M in ops:
            min_row=min(min_row,M[0])
            min_col=min(min_col,M[1])
        return min_row*min_col
