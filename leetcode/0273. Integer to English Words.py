'''
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"
Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''
class Solution:
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num==0:
            return 'Zero'
        num_s=[]
        flag=0
        while num!=0:
            tmp=num%1000
            num_s.insert(0,self.subNumberToWord(tmp))
            num=(num-tmp)/1000
            if num>0:
                if flag==0:
                    num_s.insert(0,'Thousand')
                if flag==1:
                    num_s.insert(0,'Million')
                if flag==2:
                    num_s.insert(0,'Billion')
                flag+=1
        k=0
        while k<len(num_s):
            if num_s[k]=='Zero':
                num_s.pop(k)
                if k<len(num_s):
                    num_s.pop(k)
            else:
                k+=1
        
        s=''
        for ss in num_s:
            s=s+' '+ss
        return s[1:]
    
    def subNumberToWord(self,num):
        dict_nums1={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',
                  10:'Ten',11:'Eleven',12:'Twelve',13:'Thirteen',14:'Fourteen',15:'Fifteen',
                   16:'Sixteen',17:'Seventeen',18:'Eighteen',19:'Nineteen',0:'Zero'}
        dict_nums2={2:'Twenty',3:'Thirty',4:'Forty',5:'Fifty',6:'Sixty',7:'Seventy',
                  8:'Eighty',9:'Ninety'}
        if num>=100:
            if num%100==0:
                return dict_nums1[num//100]+' '+'Hundred'
            else:
                return dict_nums1[num//100]+' '+'Hundred'+' '+self.subNumberToWord(num%100)
        if 0<=num<20:
            return dict_nums1[num]
        if num%10==0:
            return dict_nums2[num//10]
        else:
            return dict_nums2[num//10]+' '+dict_nums1[num%10]
            
