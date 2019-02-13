class Solution:
    def topKFrequent(self, nums: 'List[int]', k: 'int') -> 'List[int]':
        dictnum={}
        for num in nums:
            if num not in dictnum:
                dictnum[num]=1
            else:
                dictnum[num]+=1
        from heapq import heappop,heappush
        
        heap=[]
        i=0
        for keys in dictnum:
            if i<k:
                heappush(heap,dictnum[keys])
                i+=1
            else:
                if dictnum[keys]>heap[0]:
                    heappop(heap)
                    heappush(heap,dictnum[keys])
        
        cur=heap[0]
        rep=[]
        for keys in dictnum:
            if dictnum[keys]>=cur:
                rep.append(keys)
        return rep
