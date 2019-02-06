class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        left=0
        up=0
        right=len(matrix[0])
        down=len(matrix)
        row=0
        column=0
        rep=[]
        while left<right and up<down:
            while column<right and left<right and up<down:
                rep.append(matrix[row][column])
                column+=1
            up+=1
            column-=1
            row+=1
            while row<down and left<right and up<down:
                rep.append(matrix[row][column])
                row+=1
            right-=1
            row-=1
            column-=1
            while column>=left and left<right and up<down:
                rep.append(matrix[row][column])
                column-=1
            down-=1
            column+=1
            row-=1
            while row>=up and left<right and up<down:
                rep.append(matrix[row][column])
                row-=1
            left+=1
            row+=1
            column+=1
        return rep
