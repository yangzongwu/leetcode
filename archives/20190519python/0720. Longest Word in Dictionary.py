class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda x:[len(x),x])
        cur_word=set()
        rep=""
        
        for word in words:
            if len(word)==1 or word[:-1] in cur_word:
                cur_word.add(word)
                
                if len(word)>len(rep):
                    rep=word
                
        return rep
