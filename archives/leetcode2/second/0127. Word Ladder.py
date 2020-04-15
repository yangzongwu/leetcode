class Solution:
    def ladderLength(self, beginWord: 'str', endWord: 'str', wordList: 'List[str]') -> 'int':
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        cnt=1
        wordstack=[beginWord]
        while wordstack:
            cur=[]
            for word in wordstack:
                for k in range(len(word)):
                    for s in 'qwertyuiopasdfghjklzxcvbnm':
                        curword=word[:k]+s+word[k+1:]
                        if curword in wordList:
                            if curword==endWord:
                                return cnt+1
                            else:
                                cur.append(curword)
                                wordList.remove(curword)
            cnt+=1
            wordstack=cur
        return 0
