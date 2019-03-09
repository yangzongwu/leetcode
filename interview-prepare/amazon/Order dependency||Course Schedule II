class Solution:
    def findOrder(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        dictrequisity={}
        degree=[0]*numCourses
        for requisity in prerequisites:
            degree[requisity[0]]+=1
            if requisity[1] not in dictrequisity:
                dictrequisity[requisity[1]]=[requisity[0]]
            else:
                dictrequisity[requisity[1]].append(requisity[0])
        
        rep=[]
        for k in range(len(degree)):
            if degree[k]==0:
                rep.append(k)
        
        
        result=[]
        for precourse in rep:
            result.append(precourse)
            if precourse in dictrequisity:
                for pre_course in dictrequisity[precourse]:
                    degree[pre_course]-=1
                    if degree[pre_course]==0:
                        rep.append(pre_course)
        
        if len(result)!=numCourses:
            return []
        return result
    
