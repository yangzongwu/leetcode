class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        magazine_dict={}
        for c in magazine:
            if c not in magazine_dict:
                magazine_dict[c]=1
            else:
                magazine_dict[c]+=1
                
        for c in ransomNote:
            if c not in magazine_dict:
                return False
            else:
                if magazine_dict[c]==0:
                    return False
                magazine_dict[c]-=1
        return True
