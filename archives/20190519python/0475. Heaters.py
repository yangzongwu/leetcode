class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        rep=0
        loc=0
        cur=0
        while loc<len(houses):
            if houses[loc]<=heaters[0]:
                rep=max(rep,heaters[0]-houses[loc])
            elif houses[loc]>=heaters[-1]:
                rep=max(rep,houses[loc]-heaters[-1])
            else:
                while cur<len(heaters) and houses[loc]>=heaters[cur]:
                    cur+=1
                if cur!=len(heaters):
                    rep=max(rep,min(houses[loc]-heaters[cur-1],heaters[cur]-houses[loc]))
                else:
                    rep=max(rep,houses[loc]-heaters[cur-1])
            loc+=1
        return rep
                
            
