'''
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
 

Constraints:

1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9

'''
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dict_d={}
        for domino in dominoes:
            s1=str(domino[0])+'&'+str(domino[1])
            s2=str(domino[1])+'&'+str(domino[0])
            if s1 not in dict_d and s2 not in dict_d:
                dict_d[s1]=1
            else:
                if s1 in dict_d:
                    dict_d[s1]+=1
                else:
                    dict_d[s2]+=1    
        cnt=0
        for k in dict_d:
            cnt+=(1+dict_d[k]-1)*(dict_d[k]-1)//2
        return cnt
