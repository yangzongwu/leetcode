class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list=version1.split('.')
        version2_list=version2.split('.')
        k=0
        while k<len(version1_list) and k<len(version2_list):
            if int(version1_list[k])>int(version2_list[k]):
                return 1
            elif int(version1_list[k])<int(version2_list[k]):
                return -1
            k+=1
        if len(version2_list)==len(version1_list):
            return 0
        
        if k==len(version1_list):
            for i in range(k,len(version2_list)):
                if int(version2_list[i])!=0:
                    return -1
            return 0
        if k==len(version2_list):
            for i in range(k,len(version1_list)):
                if int(version1_list[i])!=0:
                    return 1
            return 0
        
