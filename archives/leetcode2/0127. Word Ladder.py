class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        if endWord not in wordList:
            return 0
        
        rep=[beginWord]
        wordList=set(wordList)
        cnt=1
        while wordList and rep:
            cur=[]
            for ss in rep:
                for k in range(len(ss)):
                    for s in 'qwertyuiopasdfghjklzxcvbnm':
                        tmp=ss[:k]+s+ss[k+1:]
                        if  tmp==endWord:
                            return cnt+1
                        if tmp in wordList:
                            cur.append(tmp)
                            wordList.remove(tmp)
            rep=cur
            cnt+=1   
        return 0
