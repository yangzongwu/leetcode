class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        dict_deck={}
        for num in deck:
            if num not in dict_deck:
                dict_deck[num]=1
            else:
                dict_deck[num]+=1
        target=dict_deck[deck[0]]
        
        for val in dict_deck.values():
            target=min(target,val)
        
        if target==1:
            return False
        
        
        for cur in range(2,target+1):
            if target%cur==0:
                if self.hasSameVal(cur,dict_deck):
                    return True
        return False
    
    def hasSameVal(self,target,dict_deck):
        for val in dict_deck.values():
            if val%target!=0:
                return False
        return True
