class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.key=[0]*1000001
        self.value=[0]*1000001

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.key[key]=1
        self.value[key]=value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if self.key[key]==0:
            return -1
        return self.value[key]


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        self.key[key]=0
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
