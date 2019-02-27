class Solution:
    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        dictprequisites={}
        degree=[0]*numCourses
        for prerequisite in prerequisites:
            degree[prerequisite[0]]+=1
            if prerequisite[1] not in dictprequisites:
                dictprequisites[prerequisite[1]]=[prerequisite[0]]
            else:
                dictprequisites[prerequisite[1]].append(prerequisite[0])
        
        precourse=[]
        for k in range(len(degree)):
            if degree[k]==0:
                precourse.append(k)
        for pre_course in precourse:
            if pre_course in dictprequisites:
                for course in dictprequisites[pre_course]:
                    degree[course]-=1
                    if degree[course]==0:
                        precourse.append(course)
        return sum(degree)==0
