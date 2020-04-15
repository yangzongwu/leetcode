'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows 
like this: (you may want to display this pattern in a fixed font for better legibility)

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
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rep=[]
        for k in range(numRows):
            rep.append('')
        k=0
        while k<len(s):
            row=0
            column=0
            while row<numRows and k+column<len(s):
                rep[row]+=s[k+column]
                row+=1
                column+=1
            row-=2
            while row>0 and k+column<len(s):
                rep[row]+=s[k+column]
                row-=1
                column+=1
            k=k+column
        s=''
        for ss in rep:
            s+=ss
        return s
