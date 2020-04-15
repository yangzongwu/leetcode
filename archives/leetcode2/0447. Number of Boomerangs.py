class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        rep=0
        for k in range(len(points)):
            rep+=self.subnumberOfBoomerangs(points[k],points[:k]+points[k+1:])
        return rep
        
    def subnumberOfBoomerangs(self,point,points):
        rep=0
        
        dictpoints={}
        for p in points:
            k=(p[0]-point[0])**2+(p[1]-point[1])**2
            if k not in dictpoints:
                dictpoints[k]=1
            else:
                dictpoints[k]+=1
        
        for key in dictpoints:
            if dictpoints[key]>1:
                rep+=dictpoints[key]*(dictpoints[key]-1)
        
        return rep
