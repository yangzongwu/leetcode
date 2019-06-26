class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        dict_count={}
        for candy in candies:
            if candy not in dict_count:
                dict_count[candy]=1
            else:
                dict_count[candy]+=1
        
        return  len(candies)//2 if len(dict_count)>len(candies)//2 else len(dict_count)
