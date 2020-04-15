class Solution:
    def kthSmallest(self, matrix: 'List[List[int]]', k: 'int') -> 'int':
        import heapq
        heap=[]
        cnt=0
        for row in range(len(matrix)):
            for column in range(len(matrix[0])):
                if cnt<k:
                    heapq.heappush(heap,-matrix[row][column])
                    cnt+=1
                else:
                    if -matrix[row][column]>heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap,-matrix[row][column])
        return -heap[0]
