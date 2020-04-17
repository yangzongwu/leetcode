'''
Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s. For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer, where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

 

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").
Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
 

Constraints:

1 <= queries.length <= 2000
1 <= words.length <= 2000
1 <= queries[i].length, words[i].length <= 10
queries[i][j], words[i][j] are English lowercase letters.

'''
class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        query=self.getNumberFromString(queries)
        word=self.getNumberFromString(words)
        word.sort()
        rep=[]
        for n in query:
            rep.append(self.findNumberLessThenNFromSortedList(n,word))
        return rep

    def findNumberLessThenNFromSortedList(self,n,nums):
        l,r=0,len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>n:
                r=mid-1
            else:
                l=mid+1
        return len(nums)-l


    def getNumberFromString(self,words):
        rep=[]
        for word in words:
            rep.append(self.numberFromString(word))
        return rep

    def numberFromString(self,word):
        s=list(_ for _ in word)
        s.sort()
        target=s[0]
        cnt=1
        for k in range(1,len(s)):
            if s[k]==target:
                cnt+=1
            else:
                break
        return cnt


