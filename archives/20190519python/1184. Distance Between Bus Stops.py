class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        if destination<start:
            destination,start=start,destination
            
        num1_0ToSta=self.getdistance(0,start,distance)
        num2_staToDes=self.getdistance(start,destination,distance)    
        num3_desTo0=self.getdistance(destination,len(distance),distance)
        
        return min(num2_staToDes,num1_0ToSta+num3_desTo0)
    
    
    def getdistance(self,k1,k2,distance):
        rep=0
        for k in range(k1,k2):
            rep+=distance[k]
        return rep
