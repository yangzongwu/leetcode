'''
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words. 

You may return the list in any order.

 

Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]
 

Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

'''
class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        dict_A=self.stringToDict(A)
        dict_B=self.stringToDict(B)

        rep=[]

        for key in dict_A:
            if key not in dict_B and dict_A[key]==1:
                rep.append(key)

        for key in dict_B:
            if key not in dict_A and dict_B[key]==1:
                rep.append(key)

        return rep


    def stringToDict(self,strs):
        strs_list=strs.split()
        dict_strs={}
        for ss in strs_list:
            if ss not in dict_strs:
                dict_strs[ss]=1
            else:
                dict_strs[ss]+=1
        
        return dict_strs
