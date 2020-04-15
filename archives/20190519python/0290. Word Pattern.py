class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list=str.split(" ")
        if len(pattern)!=len(str_list):
            return False
        
        used_word_list=set()
        dict_pattern={}
        for i in range(len(pattern)):
            if pattern[i] not in dict_pattern:
                if str_list[i] in used_word_list:
                    return False
                used_word_list.add(str_list[i])
                dict_pattern[pattern[i]]=str_list[i]
            else:
                if dict_pattern[pattern[i]]!=str_list[i]:
                    return False
        return True
