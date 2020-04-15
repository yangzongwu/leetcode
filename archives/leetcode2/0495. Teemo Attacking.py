class Solution:
    def findPoisonedDuration(self, timeSeries: 'List[int]', duration: 'int') -> 'int':
        left=0
        rep=0
        while left<len(timeSeries):
            j=1
            while left+j<len(timeSeries) and timeSeries[left+j]-timeSeries[left+j-1]<=duration:
                j+=1
            rep+=timeSeries[left+j-1]-timeSeries[left]+duration
            left+=j
        return rep
