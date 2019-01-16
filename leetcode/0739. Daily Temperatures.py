'''
Given a list of daily temperatures T, return a list such that, for each day in the input, 
tells you how many days you would have to wait until a warmer temperature. If there is no 
future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output 
should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an 
integer in the range [30, 100].
'''
class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        lenT=len(T)
        if lenT==1:
            return [0]
        stact_t=[T[0]]
        stact_t_index=[0]
        rep=[0]*lenT
        for k in range(1,lenT):
            while stact_t and T[k]>stact_t[-1]:
                stact_t.pop()
                pre_loc=stact_t_index.pop()
                rep[pre_loc]=k-pre_loc
            stact_t.append(T[k])
            stact_t_index.append(k)
        return rep
        
##################################################################
class Solution:
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        rep=[]
        for k in range(len(T)):
            x=self.subdailyTemperatures(T[k],T[k:])
            rep.append(x)
        return rep
    
    def subdailyTemperatures(self,t,T):
        for k in range(len(T)):
            if T[k]>t:
                return k
        return 0  
