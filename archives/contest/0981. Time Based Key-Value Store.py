class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dicts={}
        

    def set(self, key: 'str', value: 'str', timestamp: 'int') -> 'None':
        if key not in self.dicts:
            self.dicts[key]=[[timestamp,value]]
        else:
            self.dicts[key].append([timestamp,value])
           

    def get(self, key: 'str', timestamp: 'int') -> 'str':
        if key not in self.dicts:
            return ''
        else:
            lista=self.dicts[key]
            #print(lista,timestamp)
            if timestamp<lista[0][0]:
                return ''
            if timestamp>=lista[-1][0]:
                return lista[-1][1]
            if timestamp==lista[0][0]:
                return lista[0][1]
            else:
                l=0
                r=len(lista)
                while r>=l:
                    mid=(r+l)//2
                    if lista[mid][0]==timestamp:
                        return lista[mid][1]
                    elif lista[mid][0]>timestamp:
                        r=mid-1
                    else:
                        l=mid+1
                return lista[r][1]


        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
