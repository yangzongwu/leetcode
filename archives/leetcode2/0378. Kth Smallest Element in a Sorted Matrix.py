class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        import heapq
        heap=[]
        cnt=0
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                heapq.heappush(heap,matrix[row][column])
        while k>0:
            tmp=heapq.heappop(heap)
            k-=1
        return tmp
        
