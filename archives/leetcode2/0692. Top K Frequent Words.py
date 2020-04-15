class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dictword={}
        for word in words:
            if word not in dictword:
                dictword[word]=1
            else:
                dictword[word]+=1
        
        rep=[]
        for key in dictword:
            rep.append([key,dictword[key]])
            
        rep=self.sorts(rep)        
        
        res=[]
        for i in range(k):
            res.append(rep[i][0])
        return res
    
    def sorts(self,rep):
        for i in range(len(rep)):
            for j in range(i+1,len(rep)):
                if self.subsorts(rep[i],rep[j]):
                    rep[i],rep[j]=rep[j],rep[i]
        return rep
                
    def subsorts(self,a,b):
        if a[1]<b[1]:
            return True
        elif a[1]>b[1]:
            return False
        else:
            i=0
            while i<len(a[0]) and i<len(b[0]):
                if a[0][i]<b[0][i]:
                    return False
                elif a[0][i]>b[0][i]:
                    return True
                else:
                    i+=1
            if i==len(a[0]):
                return False
            else:
                return True
