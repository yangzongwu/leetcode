class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        dicts={}
        for ss in strs:
            cur=list(ss)
            cur.sort()
            s=''.join(cur)
            if s not in dicts:
                dicts[s]=[ss]
            else:
                dicts[s].append(ss)
        rep=[]
        for keys in dicts:
            rep.append(dicts[keys])
        return rep
