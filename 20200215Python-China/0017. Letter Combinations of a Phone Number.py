'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_d={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno',
        '7':'pqrs','8':'tuv','9':'wxyz'}

        if not digits:
            return []
        
        rep=[x for x in dict_d[digits[0]]]
        for num in digits[1:]:
            cur=[]
            for s1 in rep:
                for s2 in dict_d[num]:
                    cur.append(s1+s2)
            rep=cur

        return rep        
