class Solution:
    def defangIPaddr(self, address: str) -> str:
        cur=address.split('.')
        rep=""
        for str in cur:
            rep+="[.]"+str
        return rep[3:]
