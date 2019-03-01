class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dicttickets={}
        for ticket in tickets:
            if ticket[0] not in dicttickets:
                dicttickets[ticket[0]]=[ticket[1]]
            else:
                dicttickets[ticket[0]].append(ticket[1])
            
        for key in dicttickets:
            dicttickets[key].sort()
        
        rep=[]
        def dfs(dicttickets,ticket,rep):
            if ticket in dicttickets:
                while dicttickets[ticket]:
                    newticket=dicttickets[ticket].pop(0)
                    dfs(dicttickets,newticket,rep)
            rep.append(ticket)
            
        dfs(dicttickets,'JFK',rep)
        return rep[::-1]
