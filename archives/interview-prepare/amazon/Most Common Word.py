class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        cur = []
        left = 0
        while left < len(paragraph):
            while left < len(paragraph) and paragraph[left] not in 'qwertyuiopasdfghjklzxcvbnm':
                left += 1
            if left==len(paragraph):
                break
            right = left
            while right< len(paragraph) and paragraph[right] in 'qwertyuiopasdfghjklzxcvbnm':
                right += 1
            if right == len(paragraph):
                cur.append(paragraph[left:])
                break
            else:
                cur.append(paragraph[left:right])
                left = right
        

        dicts={}
        for s in cur:
            if s not in banned:
                if s not in dicts:
                    dicts[s]=1
                else:
                    dicts[s]+=1
        maxcnt,rep=0,[]
        for key in dicts:
            if dicts[key]>maxcnt:
                maxcnt=dicts[key]
                rep=[key]
            elif dicts[key]==maxcnt:
                rep+=[key]
        return rep[0]
