'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"
'''
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n==1:
            return '1'
        s='1'
        while n>1:
            s=self.subCountAndSay(s)
            n-=1
        return s
    
    def subCountAndSay(self,s):
        left,right=0,1
        rep=''
        while left<len(s):
            cnt=1
            cur_s=s[left]
            if right==len(s):
                rep+=str(cnt)+s[left]
                break
            else:
                if s[right]!=s[left]:
                    rep+=str(cnt)+s[left]
                    left=right
                    right=right+1
                else:
                    while right<len(s) and s[right]==s[left]:
                        cnt+=1
                        right+=1
                    
                    rep+=str(cnt)+s[left]
                    left=right
                    right+=1
        return rep
                  
