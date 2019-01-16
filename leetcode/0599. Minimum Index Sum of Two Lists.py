'''
Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of 
favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there 
is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.
'''
class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dictlist1={}
        for k in range(len(list1)):
            if list1[k] not in dictlist1:
                dictlist1[list1[k]]=k
        rep=[]
        for k in range(len(list2)):
            if list2[k] in dictlist1:
                if not rep:
                    rep=[list2[k]]
                    gap=k+dictlist1[list2[k]]
                else:
                    if k+dictlist1[list2[k]]<gap:
                        rep=[list2[k]]
                        gap=k+dictlist1[list2[k]]
                    elif k+dictlist1[list2[k]]==gap:
                        rep.append(list2[k])
        return rep
