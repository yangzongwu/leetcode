'''
Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        rep=[]
        self.subrestoreIpAddresses(s,rep,[])
        return rep
    def subrestoreIpAddresses(self,s,rep,tmp):
        if s and len(s)>(4-len(tmp))*3:
            return
        if not s and len(tmp)==4:
            rep.append('.'.join(tmp))
            return
        else:
            for i in range(min(3,len(s))):
                cur=s[:i+1]
                if (cur[0]=='0' and len(cur)>=2) or int(cur)>255:
                    continue
                self.subrestoreIpAddresses(s[i+1:],rep,tmp+[s[:i+1]])
        
