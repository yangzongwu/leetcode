class Solution:
    def hIndex(self, citations: 'List[int]') -> 'int':
        left=0
        right=len(citations)-1
        while left<=right:
            mid=(left+right)//2
            if mid+citations[mid]==len(citations):
                return len(citations)-mid
            elif mid+citations[mid]<len(citations):
                left=mid+1
            else:
                right=mid-1
        return len(citations)-left
