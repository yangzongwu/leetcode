'''
Given an array A of strings made only from lowercase letters, return a list of all characters that show up in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.

 

Example 1:

Input: ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: ["cool","lock","cook"]
Output: ["c","o"]
 

Note:

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] is a lowercase letter

'''
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A)==0:
            rep=[]
            for s in A:
                rep.append(s)
            return rep

        dict_A=self.stringToDict(A[0])
        
        for a in A[1:]:
            dict_a=self.stringToDict(a)
            for k in dict_A:
                if k not in dict_a:
                    dict_A[k]=0
                else:
                    dict_A[k]=min(dict_A[k],dict_a[k])
        
        rep=[]
        for k in dict_A:
            for _ in range(dict_A[k]):
                rep.append(k)
        return rep


    def stringToDict(Self,strs):
        dict_s={}
        for s in strs:
            if s not in dict_s:
                dict_s[s]=1
            else:
                dict_s[s]+=1
        return dict_s
