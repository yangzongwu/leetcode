class Solution:
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(cost)>sum(gas):
            return -1
        for k in range(len(gas)):
            res=self.subcanCompleteCircuit(gas+gas,cost+cost,k,len(gas)+k)
            if res[0]:
                return res[1]
        return -1
    
    def subcanCompleteCircuit(self,gas,cost,start,end):
        rep=0
        for k in range(start,end+1):
            rep+=gas[k]-cost[k]
            if rep<0:
                return False,-1
        return True,start
            
