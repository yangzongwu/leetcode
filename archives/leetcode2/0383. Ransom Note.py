class Solution:
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dicts={}
        for s in magazine:
            if s not in dicts:
                dicts[s]=1
            else:
                dicts[s]+=1
        for s in ransomNote:
            if s not in dicts:
                return False
            if dicts[s]==0:
                return False
            dicts[s]-=1
        return True
