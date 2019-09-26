class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        rep=0
        l=0
        while seats[l]!=1:
            l+=1
        r=len(seats)-1
        while seats[r]!=1:
            r-=1
        rep=max(l,len(seats)-1-r)
        cur=l
        while cur<r:
            if seats[cur]==1:
                cur+=1
            else:
                cnt=0
                while cur<r and seats[cur]==0:
                    cnt+=1
                    cur+=1
                rep=max(rep,(cnt-1)//2+1)
        return rep
