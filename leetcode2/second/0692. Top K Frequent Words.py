class Solution:
    def topKFrequent(self, words: 'List[str]', k: 'int') -> 'List[str]':
        dictwords={}
        for word in words:
            if word not in dictwords:
                dictwords[word]=1
            else:
                dictwords[word]+=1
        
        words=self.wordsort(list(set(words)),dictwords)
        print(words)
        return words[:k]
    
    def wordsort(self,words,dictwords):
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if dictwords[words[i]]<dictwords[words[j]]:
                    words[i],words[j]=words[j],words[i]
                elif dictwords[words[i]]>dictwords[words[j]]:
                    continue
                else:
                    if self.cmp(words[i],words[j]):
                        words[i],words[j]=words[j],words[i]
                    else:
                        continue
        return words
    
    def cmp(self,str1,str2):
        for k in range(len(str1)):
            if k<len(str2):
                if ord(str1[k])-ord(str2[k])==0:
                    continue
                elif ord(str1[k])-ord(str2[k])<0:
                    return False
                else:
                    return True
            else:
                return True
