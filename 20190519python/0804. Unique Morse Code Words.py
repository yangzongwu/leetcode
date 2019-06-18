class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s_str="abcdefghijklmnopqrstuvwxyz"
        morse_list=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        dict_morse_str={}
        for k in range(len(s_str)):
            dict_morse_str[s_str[k]]=morse_list[k]
        
        word_morse_set=set()
        for word in words:
            cur=""
            for s in word:
                cur+=dict_morse_str[s]
            word_morse_set.add(cur)
        
        return len(word_morse_set)
