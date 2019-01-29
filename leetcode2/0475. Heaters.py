class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        rep=0
        k_heaters=0
        for house in houses:
            if house<=heaters[0]:
                rep=max(rep,heaters[0]-house)
            elif house>=heaters[-1]:
                rep=max(rep,house-heaters[-1])
            else:
                j=0
                while k_heaters+j<len(heaters) and heaters[k_heaters+j]<house:
                    j+=1
                rep=max(rep,min(heaters[k_heaters+j]-house,house-heaters[k_heaters+j-1]))
                k_heaters+=j
        return rep
                
