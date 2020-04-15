class Solution:
    def toHex(self, num: int) -> str:
        if num==0:
            return "0"
        rep=""
        num_dict={10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
        for k in range(8):
            if num!=0:
                i=num&(0xf)
                num>>=4
                if i<10:
                    rep=str(i)+rep
                else:
                    rep=num_dict[i]+rep
        return rep
                
