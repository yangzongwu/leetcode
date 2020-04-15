class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rep=[]
        for word in words:
            cur=[0,0,0]
            for s in word:
                if s in 'qwertyuiopQWERTYUIOP' :
                    cur[0]=1
                elif s in 'asdfghjklASDFGHJKL':
                    cur[1]=1
                else:
                    cur[2]=1
            if sum(cur)==1:
                rep.append(word)
        return rep
