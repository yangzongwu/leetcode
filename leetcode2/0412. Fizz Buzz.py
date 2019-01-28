class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        rep=[]
        for i in range(1,n+1):
            if i%3!=0 and i%5!=0:
                rep.append(str(i))
            elif i%3==0 and i%5!=0:
                rep.append('Fizz')
            elif i%3!=0 and i%5==0:
                rep.append('Buzz')
            else:
                rep.append('FizzBuzz')
        return rep
