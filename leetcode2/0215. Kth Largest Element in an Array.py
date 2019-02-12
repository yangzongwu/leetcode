class Solution:
    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        from heapq import heappush,heappop
        heap=[]
        for i in range(k):
            heapq.heappush(heap,nums[i])
        for j in range(k,len(nums)):
            if nums[j]>heap[0]:
                heappush(heap,nums[j])
                heappop(heap)
        return heap[0]
            
