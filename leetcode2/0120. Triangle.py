class Solution:
    def minimumTotal(self, triangle: 'List[List[int]]') -> 'int':
        row=1
        while row<len(triangle):
            triangle[row][0]+=triangle[row-1][0]
            triangle[row][-1]+=triangle[row-1][-1]
            for column in range(1,len(triangle[row])-1):
                triangle[row][column]+=min(triangle[row-1][column-1],triangle[row-1][column])
            row+=1
        return min(triangle[row-1])
