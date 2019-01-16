'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
class Solution:
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        nums1=str(num1)
        nums2=str(num2)
        if len(nums1)<len(nums2):
            nums1,nums2=nums2,nums1
        listnums1=list(nums1)[::-1]
        listnums2=list(nums2)[::-1]
        flag=0
        for i in range(len(listnums2)):
            if int(listnums1[i])+int(listnums2[i])+flag>9:
                listnums1[i]=int(listnums1[i])+int(listnums2[i])+flag-10
                flag=1
            else:
                listnums1[i]=int(listnums1[i])+int(listnums2[i])+flag
                flag=0
        for i in range(len(listnums2),len(listnums1)):
            if int(listnums1[i])+flag>9:
                listnums1[i]=int(listnums1[i])+flag-10
                flag=1
            else:
                listnums1[i]=int(listnums1[i])+flag
                flag=0
        if flag==1:
            listnums1.append(flag)
        s=''
        for ss in listnums1[::-1]:
            s+=str(ss)
        return s
