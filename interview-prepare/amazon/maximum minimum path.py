#Author:YZW
'''
给一个矩阵,

先找所有从左上到右下的path.
找出每个path的最小值.
找出这些最小值中的最大值.
'''

def maxMinPath(matrix):
    for row in range(1,len(matrix)):
        matrix[row][0]=min(matrix[row-1][0],matrix[row-1][0])
    for column in range(1,len(matrix[0])):
        matrix[0][column]=min(matrix[0][column],matrix[0][column-1])
    for row in range(1,len(matrix)):
        for column in raange(1,len(matrix[0])):
            matrix[row][column]=max(min(matrix[row-1][column],matrix[row][column]),
                                    min(matrix[row][column-1],matrix[row][column]))

    return matrix[-1][-1]

A=[[8,4,3,5],[6,5,9,8],[7,2,3,6]]
print(maxMinPath(A))
