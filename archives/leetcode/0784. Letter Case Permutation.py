'''
Given a string S, we can transform every letter individually to be lowercase or 
uppercase to create another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]
Note:

S will be a string with length between 1 and 12.
S will consist only of letters or digits.
'''
class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        if not S:
            return ['']
        lists=[ss for ss in S]
        rep=[]
        for s in lists:
            tmp=[]
            if s in 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                if not rep:
                    tmp.append(s.lower())
                    tmp.append(s.upper())
                else:
                    for ss in rep:
                        tmp.append(ss+s.lower())
                        tmp.append(ss+s.upper())
            else:
                if not rep:
                    tmp.append(s)
                else:
                    for ss in rep:
                        tmp.append(ss+s)
            rep=tmp
        return rep  
