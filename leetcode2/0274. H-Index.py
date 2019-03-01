class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        if not citations:
            return 0
        
        citations.sort(reverse=True)
        
        h=len(citations)
        for k in range(h):
            if citations[k]<k+1:
                return k
        return h
        
