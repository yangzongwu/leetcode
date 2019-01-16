'''
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation 
sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''
class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        rep=[beginWord]
        curlist=[beginWord]
        cnt=1
        while rep:
            lenrep=len(rep)
            for i in range(lenrep):
                curword=rep.pop(0)
                for k in range(len(curword)):
                    for ss in 'qwertyuiopasdfghjklzxcvbnm':
                        newword=curword[:k]+ss+curword[k+1:]
                        if newword==endWord:
                            return cnt+1
                        if newword in wordList and newword not in curlist:
                            rep.append(newword)
                            curlist.append(newword)
            cnt+=1
        return 0
 ##################################################################
 class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList=set(wordList)
        if endWord not in wordList:
            return 0
        rep=[beginWord]
        curlist=set(beginWord)
        cnt=1
        while rep:
            lenrep=len(rep)
            for i in range(lenrep):
                curword=rep.pop(0)
                for k in range(len(curword)):
                    for ss in 'qwertyuiopasdfghjklzxcvbnm':
                        newword=curword[:k]+ss+curword[k+1:]
                        if newword==endWord:
                            return cnt+1
                        if newword in wordList and newword not in curlist:
                            rep.append(newword)
                            curlist.add(newword)
            cnt+=1
        return 0
