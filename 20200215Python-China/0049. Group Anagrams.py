'''
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        rep=[]
        cnt=0
        dict_s={}

        for s in strs:
            cur=[x for x in s]
            cur.sort()
            ss=''.join(cur)
            if ss in dict_s:
                rep[dict_s[ss]].append(s)
            else:
                dict_s[ss]=cnt
                rep.append([s])
                cnt+=1
        return rep
