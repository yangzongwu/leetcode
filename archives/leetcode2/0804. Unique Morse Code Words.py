class Solution:
    def uniqueMorseRepresentations(self, words: 'List[str]') -> 'int':
        ss=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        t='abcdefghijklmnopqrstuvwxyz'
        dictword={}
        for k in range(len(t)):
            dictword[t[k]]=ss[k]
            
        cnt=0
        setword=set()
        for word in words:
            tmp=''
            for ss in word:
                tmp+=dictword[ss]
            if tmp not in setword:
                setword.add(tmp)
                cnt+=1
        return cnt
