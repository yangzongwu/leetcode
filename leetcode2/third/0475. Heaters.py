class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        
        houses.sort()
        heaters.sort()
        self.left=0
        rep=0
        for house in houses:
            if house<=heaters[0]:
                rep=max(rep,heaters[0]-house)
            elif house>=heaters[-1]:
                rep=max(rep,house-heaters[-1])
            else:
                for k in range(self.left,len(heaters)):
                    if heaters[k]>house:
                        rep=max(rep,min(heaters[k]-house,house-heaters[k-1]))
                        self.left=k
                        break
        return rep
