class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1=version1.split('.')
        while list1 and int(list1[-1])==0:
            list1=list1[:-1]
        list2=version2.split('.')
        while list2 and int(list2[-1])==0:
            list2=list2[:-1]
        k=0
        while k<len(list1):
            if k==len(list2):
                return 1
            else:
                if int(list1[k])>int(list2[k]):
                    return 1
                elif  int(list1[k])<int(list2[k]):
                    return -1
                else:
                    k+=1
        if k==len(list2):
            return 0
        else:
            return -1
