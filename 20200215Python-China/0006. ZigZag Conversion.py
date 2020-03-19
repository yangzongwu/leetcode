'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
            
        s_list=['' for _ in range(numRows)]

        def dfs(s,numRows,s_list):
            if not s:
                return
            if len(s)<=numRows:
                for k in range(len(s)):
                    s_list[k]+=s[k]
                return
            elif len(s)<=numRows*2-2:
                for k in range(numRows):
                    s_list[k]+=s[k]
                for k in range(numRows,len(s)):
                    s_list[numRows*2-2-k]+=s[k]
                return
            else:
                for k in range(numRows):
                    s_list[k]+=s[k]
                for k in range(numRows,numRows*2-2):
                    s_list[numRows*2-2-k]+=s[k]
                dfs(s[(2*numRows-2):],numRows,s_list)
        
        dfs(s,numRows,s_list)

        return ''.join(s_list)
