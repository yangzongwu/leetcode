'''
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different 
letters represent different tasks. Tasks could be done without original order. Each task could be done in 
one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at 
least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.

Example:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.
 
Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].
'''
class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        dict_n={}
        for task in tasks:
            if task not in dict_n:
                dict_n[task]=1
            else:
                dict_n[task]+=1
        rep=[]
        for key in dict_n:
            rep.append(dict_n[key])
        rep.sort()
        cur=[rep.pop()]
        while rep and rep[-1]==cur[0]:
            cur.append(rep.pop())
        if len(cur)>n:
            return sum(rep)+sum(cur)
        else:
            return max(sum(rep),(cur[0]-1)*(n-(len(cur)-1)))+sum(cur)
