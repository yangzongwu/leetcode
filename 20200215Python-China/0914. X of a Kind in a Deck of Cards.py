'''
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
Example 2:

Input: deck = [1,1,1,2,2,2,3,3]
Output: false´
Explanation: No possible partition.
Example 3:

Input: deck = [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: deck = [1,1]
Output: true
Explanation: Possible partition [1,1].
Example 5:

Input: deck = [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2].
 

Constraints:

1 <= deck.length <= 10^4
0 <= deck[i] < 10^4
'''
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        if len(deck)<2:
            return False
        dict_deck={}
        cnt=0
        for k in deck:
            if k not in dict_deck:
                dict_deck[k]=1
            else:
                dict_deck[k]+=1
            cnt=max(cnt,dict_deck[k])
        list_cnt=self.dividToCnt(cnt)
        for num in list_cnt:
            flag=True
            for cur_d in dict_deck:
                if dict_deck[cur_d]%num!=0:
                    flag=False
                    break
            if flag==True:
                return True
        return False

    def dividToCnt(self,cnt):
        rep=[0]*(cnt+1)
        rep[0]=1
        rep[1]=1
        for i in range(2,cnt//2+1):
            if rep[i]==1:
                continue
            else:
                for k in range(2,cnt//i):
                    rep[k*i]=1
        res=[]
        for k in range(len(rep)):
            if rep[k]==0:
                res.append(k)
        return res


