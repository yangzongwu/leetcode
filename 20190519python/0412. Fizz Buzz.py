class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        rep=[]
        for i in range(1,n+1):
            if i%15==0:
                rep.append("FizzBuzz")
            elif i%5==0:
                rep.append("Buzz")
            elif i%3==0:
                rep.append("Fizz")
            else:
                rep.append(str(i))
        return rep
