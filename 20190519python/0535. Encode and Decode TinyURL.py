class Codec:
    
    def __init__(self,):
        self.dictToL={}
        self.dictToS={}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.dictToS:
            return self.dictToS[longUrl]
        rep=""
        strs="1234567890qwertyuiopasdfghjklzxcvbnm"
        for i in range(7):
            for k in random.choice(strs):
                rep+=k
        self.dictToS[longUrl]=rep
        self.dictToL[rep]=longUrl
        return rep
                

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        return self.dictToL[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
