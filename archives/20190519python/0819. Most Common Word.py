class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for i in '!?\',;.':
            paragraph=paragraph.replace(i,' ')
        paragraph=paragraph.lower()
        p_list=paragraph.split(' ')
        dict_word={}
        for word in p_list:
            if word and word not in banned:
                if word not in dict_word:
                    dict_word[word]=1
                else:
                    dict_word[word]+=1
        cnt=0
        cur=''
        for k in dict_word:
            if dict_word[k]>cnt:
                cnt=dict_word[k]
                cur=k
        return cur
