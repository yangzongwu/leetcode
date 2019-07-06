class Solution:
    def findDiagonalOrder(self, matrix):
        if not matrix:
            return []

        row = 0
        col = 0
        rep = []
        flag = 0
        rep.append(matrix[row][col])
        while row < len(matrix) and col < len(matrix[0]):
            if (row == len(matrix) - 1 and col == len(matrix[0]) - 2) or (
                    row == len(matrix) - 2 and col == len(matrix[0]) - 1):
                rep.append(matrix[-1][-1])
                break
            if flag == 0:
                if col<len(matrix[0])-1:
                    col += 1
                else:
                    row+=1
                tmp = self.decreaseOrder(matrix, row, col, rep)
                row, col = tmp[0], tmp[1]
                flag = 1
            elif flag == 1:
                if row<len(matrix)-1:
                    row += 1
                else:
                    col+=1
                tmp = self.increaseOrder(matrix, row, col, rep)
                row, col = tmp[0], tmp[1]
                flag = 0
        return rep

    def decreaseOrder(self, matrix, row, col, rep):
        while row < len(matrix) and col >= 0:
            rep.append(matrix[row][col])
            row += 1
            col -= 1
        return [row - 1, col + 1]

    def increaseOrder(self, matrix, row, col, rep):
        while row >= 0 and col < len(matrix[0]):
            rep.append(matrix[row][col])
            row -= 1
            col += 1
        return [row + 1, col - 1]
