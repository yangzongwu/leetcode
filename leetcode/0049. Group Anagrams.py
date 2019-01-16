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
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts={}
        rep=[]
        i=0
        for s in strs:
            ss=''.join(sorted(s))
            if ss not in dicts:
                dicts[ss]=i
                i+=1
                rep.append([s])
            else:
                rep[dicts[ss]].append(s)
        return rep
